`/home/widehyo/.bashrc`

```rc
export PATH="$PATH:~/shell"
alias runjar='java -jar'
```

`/home/widehyo/ktc`
```bash
#!/bin/bash

kt_file_name=${1##*/}
jar_file_name=${kt_file_name/.kt/.jar}
echo kotlinc $1 -include-runtime -d $jar_file_name
kotlinc $1 -include-runtime -d $jar_file_name
```

`/home/widehyo/runkt`
```bash
#!/bin/bash

kt_file_name=${1##*/}
jar_file_name=${kt_file_name/.kt/.jar}
echo kotlinc $1 -include-runtime -d $jar_file_name && echo java -jar $jar_file_name
kotlinc $1 -include-runtime -d $jar_file_name  && java -jar $jar_file_name
```

reading/10_Kotlin_Programming/practice on  main [✘!?] via ☕ v21.0.6 via 🅺 v2.1.10 ❯ !!
runkt HelloKotlin.kt
kotlinc HelloKotlin.kt -include-runtime -d HelloKotlin.jar
java -jar HelloKotlin.jar
Hello Kotlin!


```chatgpt
practice/KotlinProgramming/src on  main [✘!?] via 🅺 v2.1.10 ❯ tree .
.
├── File1.kt
├── chap02
│   └── section1
│       ├── UserClassImport.kt
│       ├── defaultPackage.jar
│       └── defaultPackage.kt
└── com
    └── example
        └── edu
            └── Person.kt

practice/KotlinProgramming/src on  main [✘!?] via 🅺 v2.1.10 ❯ cat com/example/edu/Person.kt
package com.example.edu

class Person(val Name: String, val age: Int)

practice/KotlinProgramming/src on  main [✘!?] via 🅺 v2.1.10 ❯ cat chap02/section1/UserClassImport.kt
package chap02.section1

import com.example.edu.Person

fun main() {
    val user1 = Person("Gildong", 30)

    println(user1.name)
    println(user1.age)

}

kotlinc UserClassImport.kt -include-runtime -d UserClassImport.jar
import com.example.edu.Person
           ^^^^^^^
UserClassImport.kt:6:17: error: unresolved reference 'Person'.
    val user1 = Person("Gildong", 30)
                ^^^^^^

resolve it
ChatGPT의 말:
The issue you're facing occurs because Kotlin cannot find the Person class, which is defined in the com.example.edu package. This is happening because you are trying to compile UserClassImport.kt separately, but you haven't specified the classpath where Person.kt is located.

To resolve this issue, you need to tell the Kotlin compiler where the Person.kt file (and the package it belongs to) is located, so that it can resolve the import.

Steps to resolve the issue:
Compile the Person.kt file first: Before you compile UserClassImport.kt, you need to compile the file that contains the Person class (Person.kt) so that it is available for use in the compilation of UserClassImport.kt.

Compile both files together: When you run the kotlinc command, make sure to include the com/example/edu/Person.kt file in the classpath so that it can resolve the Person class.

Here's what you should do:

Compile Person.kt:

bash
복사
kotlinc com/example/edu/Person.kt -d Person.jar
Compile UserClassImport.kt and include the classpath:

bash
복사
kotlinc -cp .:Person.jar chap02/section1/UserClassImport.kt -include-runtime -d UserClassImport.jar
The -cp .:Person.jar option adds the current directory (.) and Person.jar to the classpath, allowing the Person class to be resolved.
Run the compiled program:

nginx
복사
java -jar UserClassImport.jar
This will allow the Kotlin compiler to locate Person.kt and successfully compile UserClassImport.kt.

Key Notes:
The -cp option in kotlinc is crucial for setting the classpath.
Ensure the file paths are correct, relative to where you're running the kotlinc command.
Let me know if you need further help!

bash path expansion for find filename com/example/edu/Person.kt => Person.kt. it would like to ${##} or ${//} i forgot it
ChatGPT의 말:
In Bash, you can use parameter expansion to extract parts of a file path, and it sounds like you're looking for a way to extract the filename from the full path, like com/example/edu/Person.kt to Person.kt.

The syntax you're looking for is:

${variable##*/} — This removes everything up to and including the last /, leaving only the file name.
Here's how you can do it:

bash
복사
filepath="com/example/edu/Person.kt"
filename="${filepath##*/}"
echo $filename
This will output:

복사
Person.kt
Explanation:
${filepath##*/}: This expands the variable filepath and removes everything up to and including the last /, leaving just the filename.
If you want to remove the file extension (e.g., .kt), you can use another parameter expansion like this:

bash
복사
filename_without_extension="${filename%%.*}"
echo $filename_without_extension
This will give you:

nginx
복사
Person
Let me know if you need further clarification!

나의 말:
if i want just filename extension?
ChatGPT의 말:
If you want just the file extension (e.g., .kt from Person.kt), you can use parameter expansion like this:

bash
복사
filepath="com/example/edu/Person.kt"
extension="${filepath##*.}"
echo $extension
Explanation:
${filepath##*.}: This will extract everything after the last . in the filename, which is typically the file extension.
So if filepath="com/example/edu/Person.kt", this will output:

nginx
복사
kt
If you want to include the dot (.) in the extension (e.g., .kt), you can modify it slightly:

bash
복사
extension=".${filepath##*.}"
echo $extension
This will output:

복사
.kt
Let me know if that helps!
```


practice/KotlinProgramming/src on  main [✘!?] via ☕ v21.0.6 via 🅺 v2.1.10 ❯ java -cp .:Person.jar:UserClassImport.jar chap02.section1.UserClassImportKt
Gildong
30


12209  2025-03-11 20:08:45 ktc com/example/edu/Person.kt
12220  2025-03-11 20:19:51 kotlinc -cp .:Person.jar chap02/section1/UserClassImport.kt -include-runtime -d UserClassImport.jar
12228  2025-03-11 20:23:57 java -cp .:Person.jar:UserClassImport.jar chap02.section1.UserClassImportKt


```
can i include glob expression **/*.jar with -cp option?
ChatGPT의 말:
Yes, you can use a glob pattern to include multiple .jar files with the -cp (classpath) option, but there are some caveats based on the shell you're using. For most shells like Bash, you can use the **/*.jar glob pattern, but you need to make sure your shell is configured to handle globbing correctly.

Using Glob Pattern with -cp:
Bash or Zsh (with globstar enabled): If you're using Bash or Zsh, you can enable the globstar option in Bash to support recursive globbing (**) by running:

bash
복사
shopt -s globstar  # Enables globstar in bash
Then, you can use the following command to include all .jar files recursively:

bash
복사
java -cp "path/to/directory/**/*.jar" com.example.Main
Explanation:

"path/to/directory/**/*.jar" will match all .jar files in the specified directory and all its subdirectories.
If you're using Zsh, the globstar option is enabled by default, so you can directly use:

bash
복사
java -cp "path/to/directory/**/*.jar" com.example.Main
With Wildcards: If globstar is not enabled, you can still use regular wildcards like this:

bash
복사
java -cp "path/to/directory/*.jar:path/to/another/directory/*.jar" com.example.Main
This command will include all .jar files in specific directories, but it won't recurse into subdirectories unless you manually specify them.

Using find Command (for non-globstar shells):
If you're on a system where globstar is not enabled (or using a shell that doesn't support it), you can use the find command to gather all .jar files and then pass them to the -cp option:

bash
복사
java -cp "$(find path/to/directory -name '*.jar' -print | tr '\n' ':')" com.example.Main
Explanation:

find path/to/directory -name '*.jar' finds all .jar files in the given directory and its subdirectories.
tr '\n' ':' converts the newline-separated list of files into a colon-separated list suitable for the classpath.
Final Example:
If you have your .jar files in ./lib/ and you want to include all of them, you can do it like this:

bash
복사
java -cp "./lib/**/*.jar" com.example.Main
Or with find:

bash
복사
java -cp "$(find ./lib -name '*.jar' -print | tr '\n' ':')" com.example.Main
Important Notes:
If you're on Windows, you'll need to use semicolons (;) instead of colons (:) to separate classpath entries.
Make sure to quote the glob pattern ("...") to prevent shell expansion issues, especially when dealing with complex paths.
Let me know if you need any further clarification!
```

