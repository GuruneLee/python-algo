# solution
- v를 p구간별로 구분해서, 각 구간에 l일 만큼 캠핑장을 이용 -> (v//p)*l
- p로 구분하고 남은 공간에도 최대 l일 만큼 이용할 수 있음 -> min(l,v%p)

# trouble shooting
- 남은 공간이 l 보다 많을 수 있다는 사실을 깜빡함