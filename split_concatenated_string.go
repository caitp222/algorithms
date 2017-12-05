package main

import (
  "strings"
  "fmt"
)

func concatenatedBreakUp(str string, arr []string) []string {
  if (len(str) == 0) {
    return make([]string,0)
  }
  i := 0
  for (i <= len(str)) {
    if lookUp(str[:i], arr, 0, len(arr) - 1) {
      remainder := concatenatedBreakUp(str[i:], arr)
      if remainder != nil {
        remainder = append(remainder, str[:i])
        return remainder
      }
    }
    i += 1
  }
  return nil
}

func lookUp(word string, dictionary []string, low int, high int) bool {
  wordLower := strings.ToLower(word)
  for low <= high {
    mid := (low + high)/2
    if wordLower == strings.ToLower(dictionary[mid]) {
      return true
    } else if wordLower < strings.ToLower(dictionary[mid]) {
      high = mid - 1
      return lookUp(word, dictionary, low, high)
    } else if wordLower > strings.ToLower(dictionary[mid]) {
      low = mid + 1
      return lookUp(word, dictionary, low, high)
    }
  }
  return false
}

func main() {
  dict := []string{"aardvark", "beastly", "bigger", "christian", "Favor", "favorite", "ghost", "ghostly", "person", "personalize", "plastic", "unnecessary"}
  str := "aardvarkpersonalizeunnecessaryghostFavorbiggerbeastly"
  fmt.Println(concatenatedBreakUp(str, dict))
}
