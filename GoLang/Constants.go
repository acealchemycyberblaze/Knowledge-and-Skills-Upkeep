// constants are declaired like variables but with the const keyword
// constants can only be character, string, boolean, or numeric value and
// cannot be declaired using the := syntax. an untyped constant takes the type needed by its context
const Pi = 3.14
const(
  StatusOK=200
  StatusCreated=201
  StatusAccepted=202
  StatusNonAuthoritativeInfo =203
  StatusNoContent=204
  StatusResetContent=205
  StatusPartialContent=206
)



// https://play.golang.org/p/fPlqsffS-J

package main
import "fmt"

const(
  Name = Olivier
  Truth = false
  Big = 1 << 60
  Small = Big >>59
)
func main(){
  const Greeting = ""
  fmt.Println(Greeting)
  fmt.Println(Name)
  fmt.Println(Truth)
  gmt.Println(Big)
}
