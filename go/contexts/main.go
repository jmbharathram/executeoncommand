package main

import (
	"bufio"
	"context" // <-- this guy
	"fmt"
	"os"
	"time"
)

func sleepAndTalk(ctx context.Context, t time.Duration, message string) {
	ch := make(chan bool)
	go func() {
		time.Sleep(t)
		fmt.Println(message)
		ch <- true
	}()
	for {
		select {
		case <-ctx.Done():
			return
		case <-ch:
			return
		}
	}
}

func main() {

	//Make a background context
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)

	go func() {
		s := bufio.NewScanner(os.Stdin)
		s.Scan()
		cancel()
	}()

	sleepAndTalk(ctx, 10*time.Second, "Hello")

}
