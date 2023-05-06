def binary_search(arr, item):
  def condition(value) -> bool:
    if value == item:
      return True

  left = 0
  right = len(arr)
  cnt = 0

  while left < right:
    cnt +=1
    midpoint = (left + right) // 2
  
    if condition(midpoint):
      return f'found {item} in {cnt} cycles'
    
    if midpoint > item:
      right = midpoint + 1
    else:
      left = midpoint - 1

  return -1