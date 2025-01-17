def solution(mystring):
  answer = ''
  for a in mystring:
    if a < 'l':
      answer += 'l'
    else:
      answer += a
  return answer
