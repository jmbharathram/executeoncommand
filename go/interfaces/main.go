// Go interfaces

package main

import (
	"fmt"
)

type Speak interface {
	greet()
}

type Dog struct {
	Name string
}

type Cat struct {
	Name string
}

func (c Cat) greet() {
	fmt.Println(c.Name, "says meow!")
}

func (d Dog) greet() {
	fmt.Println(d.Name, "says woof!")
}

func main() {

	var s Speak

	d1 := Dog{"Oscar"}
	s = d1 // implicit implementation
	s.greet()

	c1 := Cat{"Mittens"}
	s = c1 // runtime polymorphism
	s.greet()

}
