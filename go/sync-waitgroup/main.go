// In this lesson, let's look at sync.WaitGroup

package main

import (
	"fmt"
	"sync"
	"time"
)

func myFunc2(wg *sync.WaitGroup) {
	time.Sleep(1 * time.Second)
	fmt.Println("Hello from myFunc2!")
	wg.Done()
}

func myFunc1(wg *sync.WaitGroup) {
	time.Sleep(1 * time.Second)
	fmt.Println("Hello from myFunc1!")
	wg.Done()
}

func main() {
	
	var wg sync.WaitGroup
	wg.Add(2)
	//go myFunc1()
	//time.Sleep(3*time.Second)
	go myFunc1(&wg)
	go myFunc2(&wg)
	wg.Wait()
	fmt.Println("Bye!")
}
