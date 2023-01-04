function lengthOfLastWord(str) {
  let count = 0;
  for(let i = str.length - 1; i >= 0; i--) {
    if(count !== 0 && str[i] === ' ') return count;
    if(str[i] !== ' ') count += 1;
  }
  return count;
}

console.log(lengthOfLastWord(" Hell world  "));
