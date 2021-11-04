lang = dict({1:"Go, Go is a statically typed, compiled programming language designed at Google", 2:"C#, C# is a general-purpose, multi-paradigm programming language.", 3:"LISP, Lisp is a family of programming languages with a long history and a distinctive, fully parenthesized prefix notation.",4:"ASP.NET , ASP.NET is an open-source, server-side web-application framework designed for web development to produce dynamic web pages", 5:"C, C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system."})

ord_list = [3, 2, 4, 1, 5] 

res = dict()
for key in ord_list:
    res[key] = lang[key]
    
    
print(str(res)) 