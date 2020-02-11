package main

import "fmt"

//variable and infered types
// the var statment declares a list of variables with the type declared last
var (
	name, location string
	age            int
)

// variables can also be declared one by one
var name string
var age int
var location string

// a variable can include initializers, one per variables
var (
	name     string = "prince boschko"
	age      int    = 20
	location string = "toronto"
)

// you can initialize variables on the same line
var (
	name, location, age = "prince boschko", "toronto", 20
)

// inside a function the := short assignment statment can be used in place of
// a var declaration with implicit type
func main() {
	name, location := "prince boschko", "toronto"
	age := 20
	fmt.Printf("%s (%d) of %s", name, age, location)
}
