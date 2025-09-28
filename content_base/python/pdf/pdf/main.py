from weasyprint import HTML

HTML(filename='a.html').write_pdf('a.pdf')
print('done')
