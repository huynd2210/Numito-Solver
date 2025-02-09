Solver for the puzzle game: Numito
App store: https://apps.apple.com/us/app/numito/id1569146063 <br>
Google Play: https://play.google.com/store/apps/details?id=com.juan.ma.nudoku&hl=en-US
![image](https://github.com/user-attachments/assets/18582f0a-3615-4c4f-a4d5-d0dec05f622c?s=30)

Example:
```
if __name__ == '__main__':
    input = "59/*53-+853+327"
    target = [12,13]
    # target = "="
    print(solve(input, target))
```
```
Output:
{12: ['5/5+8+3', '5*3-5+2'], 13: ['5/5+5+7', '5*3-5+3', '9/3+8+2', '9/3+3+7']}
```
For puzzles with '=' use '=' for target. 
To run simply:
```
python solver.py
```



  
