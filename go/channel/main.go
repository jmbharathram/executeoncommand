package main

import "fmt"

// Example 0
func dummy_func() {
	fmt.Println("dummy_func")
}
func main() {
	go dummy_func()
    fmt.Println("end of main")
}


// Example 1

package main

import "fmt"

func dummy_func(ch chan int) {
    // receive a value from channel
    val := <-ch
	fmt.Println(val)
}
func main() {
    // create a channel
	ch := make(chan int)
    // trigger a parallel go routine
	go dummy_func(ch)
    // send a value into the channel
	ch <- 10
}

// Example 2

package main

import (
    "fmt"
    //"flag"
)

func dummy_func(ch chan int) {
    // receive a value from channel
    val := <-ch
	fmt.Println(val)

    //send a value again
    ch <- val*2
}
func main() {
    fmt.Println("Welcome to main function")
    
    //flag statements for user input
    var input_value int
    input_value = 10
    //flag.IntVar(&input_value, "v", 10, "Input value to send/receive via channel." )
    //flag.Parse()

    // create a channel
	ch := make(chan int)

    // trigger a parallel go routine
	go dummy_func(ch)
    
    // send a value into the channel
	ch <- input_value

    // receive a value from channel
    response := <- ch
    fmt.Println(response)

}

// example 3


package main

import(
"fmt"
"time"
"math/rand"
)

func routine1(ch chan int, min int, max int) {

    rand.Seed(time.Now().UnixNano())
    t := rand.Intn(max - min) + min
    fmt.Println("routine 1 is waiting: ", t, "secs")
    time.Sleep(time.Duration(t)*time.Second)

    ch <- t
}

func routine2(ch chan int, min int, max int) {

    rand.Seed(time.Now().UnixNano())
    t := rand.Intn(max - min) + min
    fmt.Println("routine 2 is waiting: ", t, "secs")
    time.Sleep(time.Duration(t)*time.Second)

    ch <- t
}

func main(){

min := 1
max := 10

ch1:= make(chan int)
ch2:= make(chan int)

go routine1(ch1, min, max)
go routine2(ch2, min, max)

select{

case <- ch1:
    fmt.Println("routine 1 finished")

case <- ch2:
    fmt.Println("routine 2 finished")
}

fmt.Println("end of main function")

}
