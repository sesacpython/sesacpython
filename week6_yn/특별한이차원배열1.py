def solution(n):
  answer = []
  for i  n range(n):
      row = []
      for j in range(n):
          if i  ==j:
              row.append(1)
          else:
              row.append(0)
      answer.append(row)
return answer
