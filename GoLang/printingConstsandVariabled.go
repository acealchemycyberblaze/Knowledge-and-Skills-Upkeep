// to print the value of variables & constants use the print and println functions
// the more idiomatic and flexible way is to use the fmt package

func main(){
  typeModle := 6
  fmt.Println(typeModle)
}

// fmt.println prints the passes in variables values and appends a newline
// fmt.printf is used when you want to print one or multiple values using
// a defined format specifier

func main(){
  name := "boschko-ten"
  aka := fmt.Sprintf("Number %d" 6)
  fmt.Printf("%s is also known as %s", name, aka)
}
//=> boschko-10 is also known as Number 6
