---
title: clojure kickstart
tags: #clojure #notes
---
# clojure

## Language semantics TLDR
- lisp dialect
	- code as data and data as code(provides awesome metaprogramming features)
	- no operator precedence in prefix notation
	- application is sometimes easier
	- too many paranthesis
- based on JVM(hosted environment such as nodejs is also supported)
- java interops(Java is OG in terms of backward compatibility)
- immutable and lazy in some aspects ?
- concurrency via CSP(channels as backbone)
- dynamically typed

Clojure is a general purpose high level, dynamically typed, lazily evaluated, lisp dialect based on JVM. We will break down these one at a time.



[Clojure learn x in y minutes](https://learnxinyminutes.com/docs/clojure/)
[Clojure wikipedia](https://en.wikipedia.org/wiki/Clojure)

### java and backward comp.
https://www.reddit.com/r/AskProgramming/comments/f6xlps/why_is_java_praised_for_its_backward/

Backward compatibility is not always a good thing. Some languages have features that just shouldn't have ever been released. Keeping them in the language purely for backwards compatibility is questionable

There are 2 things that Java has over JavaScript in this regard

\- Java was better designed at day 1. JavaScript was put together very quickly with many features that may not have been a good idea

\- Java is a compiled language, so only the compiler needs to remain backwards compatible. The JVM can be upgraded freely, so long as the compilers are upgraded with it. JavaScript is an interpreted language and does not have this luxury. All interpreters need to remain backwards compatible and support potentially unwanted features

On another note, if you want a good example of languages being praised for dropping backwards compatibility, look at PHP 7. They dropped the mysql-library which was notorious for it's security vulnerabilities
