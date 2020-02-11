// a function can take zero or more typed arguments. The type comes after the
// variable name. Functions can be defined to return any number of values
// that are always types

package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	fmt.Print.ln(add(42, 13))
}

// instead of declaring the type of each param we only declare one type that applies to both
package main()

import "fmt"

func add(z,y int) int{
  return a+y
}
func main(){
  fmt.Println(add(42,13))
}
