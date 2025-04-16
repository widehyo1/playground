" Vim function to check for project root and generate .tags if not found
function! GenerateTags()
    " Find the pyproject.toml file (project root)
    let pyproject_file_path = findfile('pyproject.toml', expand("%:p:h") . ";")
    let project_root = fnamemodify(pyproject_file_path, ":p:h")

    if project_root == ""
        echo "pyproject.toml not found!"
        return
    endif

    " Check if .tags file exists in the project root
    let tags_file = project_root . "/.tags"

    " if !filereadable(tags_file)
        " If .tags doesn't exist, generate it using ctags
        " echo 'Generating .tags file...'
        " let cmd = 'cd ' . project_root . ' && ctags -R --languages=Python -f .tags .'
        " call system(cmd)
    let cmd = 'cd ' . project_root . ' && ctags -R --languages=Python -f .tags .'
    call system(cmd)
    " else
    "     echo '.tags file found, skipping generation.'
    " endif
endfunction

" Vim function to generate .pyfullnames file
function! PoetryHelpPopup()
    " Find the project root and ensure .tags exists
    call GenerateTags()

    " Get the current buffer's file path
    let current_file = expand("%:p")

    " Get the project root by finding pyproject.toml
    let pyproject_file_path = findfile('pyproject.toml', expand("%:p:h") . ";")
    let project_root = fnamemodify(pyproject_file_path, ":p:h")

    if project_root == ""
        echo "pyproject.toml not found!"
        return
    endif

    " Get the path to .tags file
    let tags_file = project_root . "/.tags"

    " Use the Python script to process imports
    let imports = system('python3 ' . expand('~/.vim/util/process_imports.py') . ' ' . current_file)

    " Process the .tags file with awk to generate class, method, and function names
    let awk_command = 'awk -f ~/.vim/util/ctags_to_fullnames.awk ' . tags_file
    let tags_fullnames = system(awk_command)

    let s:pyhelp_dict_list = []

    let full_names = []
    let seen = {}

    for full_name in split(imports, '\n') + split(tags_fullnames, '\n')
      if !has_key(seen, full_name)
        let seen[full_name] = 1
        call add(full_names, full_name)
      endif
    endfor

    for full_name in filter(full_names, { _, val -> val =~ expand('<cword>') .. '$' })
        if expand('<cword>') != full_name->matchstr('[^\.]*$')
          continue
        endif
        let pyhelp_dict = {}
        let pyhelp_dict['text'] = full_name
        let cmd = 'PAGER=cat poetry run python -m pydoc ' . full_name
        let pyhelp_dict['cmd'] = cmd
        call add(s:pyhelp_dict_list, pyhelp_dict)
    endfor

    let @a = ''
    let @A = DictListToString(s:pyhelp_dict_list)

    if len(s:pyhelp_dict_list) == 1
      call OpenPydocPopup(s:pyhelp_dict_list[0])
      return
    endif

    " popup settings
    let width  = float2nr(&columns * 0.8)
    let height = float2nr(&lines * 0.8)
    " let opts = {
    "       \ 'minwidth': width,
    "       \ 'minheight': height,
    "       \ 'maxwidth': width,
    "       \ 'maxheight': height,
    "       \ 'cursorline': 1,
    "       \ 'scrollbar': 1,
    "       \ 'callback': 'OpenPydocPopupCallback'
    "       \ }
    " call popup_menu(s:pyhelp_dict_list, opts)
    call ShowPydocPopup()
endfunction

function! OpenPydocPopup(target_dict)
  let lines = system(a:target_dict['cmd'])
  let popup_content = lines->split('\n')

  " Determine the popup dimensions relative to the editor size.
  let width  = float2nr(&columns * 0.8)
  let height = float2nr(&lines * 0.8)


  let start_row  = float2nr(&lines * 0.1)
  let start_col = float2nr(&columns* 0.1)

  " Set popup options:
  " - 'line' and 'col' positions relative to the cursor.
  " - 'minwidth'/'maxwidth' and 'minheight'/'maxheight' keep it fixed sized.
  " - 'scrollbar' adds a vertical scrollbar.
  " - 'border' and 'padding' customize the look.
  let opts = {
        \ 'minwidth': width,
        \ 'minheight': height,
        \ 'maxwidth': width,
        \ 'maxheight': height,
        \ 'scrollbar': 1,
        \ 'border': [],
        \ 'padding': [0,1,0,1],
        \ 'filter': funcref('ScrollPopupFilter'),
        \ 'filtermode': 'n',
        \ 'mapping': v:false
        \ }

  let @a = ''
  " let @a = len(popup_content) .. ' ' .. height

  if len(popup_content) <= height
    let @b = ''
    " let @b = 'if len(popup_content) <= height'

    let opts['scrollbar'] = 0
    let opts['filter'] = funcref('PopupFilter')
  endif

  let @c = ''
  " let @c = DictToString(opts)

  " Create and show the popup window.
  call popup_create(popup_content, opts)
  " let @a = ''
  " let @a = ListToString(popup_content, '###')
  " call popup_create(popup_content, {})

endfunction

function! ShowPydocPopup()
  call timer_start(10, {-> popup_menu(s:pyhelp_dict_list, { 'callback': 'OpenPydocPopupCallback' }) })
endfunction

function! OpenPydocPopupCallback(id, result)
  let target_dict = s:pyhelp_dict_list[a:result-1]
  call OpenPydocPopup(target_dict)
  " echo target_dict
endfunction


