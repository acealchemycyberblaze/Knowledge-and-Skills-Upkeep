// every go program is made up of packages. Programs start running in package main

package main
func main(){
  print("hello, world!\n")
}

//if youre writing an exedcutable vs a libray then you need to define a main packages
// and a main() function which will be the entry point of your software.

// by convention the package name is the last element odf the import path. for
// instance the "math/rand" package comprises files that begin with the statement package rand

import (
  "fmt"
  "math/rand"
)
