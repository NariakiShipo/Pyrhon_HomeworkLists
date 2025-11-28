# 032 電路－解題思路
### 1.  判斷輸入二進制的8bit直到輸入為-1
### 2. C(M)的邏輯處理
$$\text{Count}(M) =
\begin{cases}
0 & \text{if } M \le 1 \\
1 + \text{Count}(M/2) & \text{if } M \text{ is even} \\
2 + \text{Count}((M+1)/2) + \text{Count}((M-1)/2) & \text{if } M \text{ is odd}
\end{cases}$$
### 3. R 記錄器紀錄回饋次數
### 4. 將輸入的二進制轉換成三進制6bit的格式並輸出