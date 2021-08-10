# File IO

## File 입출력
  - file 생성 및 작성 : open('파일 경로', 'w')
  - file 읽어들이기 : open('파일 경로', 'r')
  - file 내용 추가 : open('파일 경로', 'a')

```python
# file 입출력
fw = open('/Users/limjunhyuk/Documents/BOJ/BOJ_Solve/BOJ_PYTHON/newFile.txt', 'w')
for i in range(1, 11):
    data = f"{i} line.\n"
    fw.write(data)
fw.close()
## write()

fr = open('/Users/limjunhyuk/Documents/BOJ/BOJ_Solve/BOJ_PYTHON/newFile.txt', 'r')
while True:
    line = fr.readline()
    if not line: break
    print(line, end='')
fr.close()
## readline()
```
