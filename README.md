# Supaero SDD CTF 2025

Question and data repository for the [2025 Capture the Flag](https://supaerodatascience.github.io/DE/ctf.html).

[Leaderboard](http://34.163.196.38/)

Server IP: 34.163.196.38

## Questions - 2025 edition

1 | Where is the `curl` executable located? Some systems vary, if your answer is incorrect, try a common alternative.

2 | What is the linux command used for reading manuals?

3 | Where is the `less` executable located?

4 | What is the key for scrolling down by one half of screen size in `less`?

5 | What is the longer name of the `-K` flag to `curl`?

6 | What is the `cp` command flag allowing for copying directories?

7 | What is the `ls` command flag used for human-readable output?

8 | What is the `mv` command flag which will interactively prompt before overwriting files?

9 | What is the `cat` command flag which shows line numbers?

10 | If the variable `STRING` is set to `banana`, what does the command `echo ${STRING:4}$` return?

11 | If the variable `a` is set to 3 and `b` is set to 4, what does the command `if [[ $a -le $b ]]; then echo $a; else echo $b; fi` return?

12 | If the variable `p` is set to `(3 1 4 1 5 9)`, what does the command `echo $((${p[0]} * ${p[2]}))` return?

13 | What is the `grep` command flag used to select _non-matching_ lines?

14 | What is the longer name of the `-c` flag to `grep`?

15 | How many lines are in `file_a.txt`?

16 | What does the command `head -n 10 file_a.txt | wc -l` return?

17 | How many words in `file_a.txt` start with the letter "d"?

18 | How many words are in `file_a.txt` that contain only 4 letters?

19 | What is the last word in `file_b.txt`?

20 | What is the line number of the word "helicopter" in `file_b.txt`?

21 | How many characters are in `file_c.txt`?

22 | How many words contain "croissant" inside them in `file_c.txt`?

23 | What word is at the same line in `file_c.txt` as the word "sheep" is in `file_a.txt`?

24 | What is the second word in `file_c.txt` which contains the letter `x`?

25 | What is the size of `file_a.txt` in bytes?

26 | What is the command to display files in the current directory?

27 | What is the find command flag that limits the search to a certain depth in directories?

28 | What command would you use to display all currently running processes?

29 | What is the environment variable used to define the location of executable programs?

30 | What is the flag for diff that ignores case differences?

### Linux tools

31 | What is the `apt` command used to install available updates?

32 | What is the letter of the `apt-get` command flag to perform a test run of the installation that does not actually change the system?

33 | What is the file which lists locations that `apt` fetches packages from?

34 | What is the name of the first column in `top` by default?

35 | What is the letter of the command in `top` to kill a process?

36 | What is the `tmux` command to list all running sessions?

37 | What is the `tmux` command to use an existing session?

38 | What is the letter of the tmux key binding to create a new window inside `tmux`?

39 | What is the letter of the tmux key binding to leave the current client without stopping it?

40 | If you run `tmux` on a remote server and then disconnect, will the `tmux` session end? "yes" or "no"

41 | What is the name for the tutorial command to learn `vim`?

42 | What is the name of the mode `vim` starts in by default?

43 | What is the command to quit vim, without saving changes?

44 | What is the letter used to navigate up in `vim`?

45 | What is the file used for a user's `vim` configuration?

46 | What is the flag for the apt-get command to purge a package, including its configuration files?

47 | What is the apt command to update the list of available packages from sources listed in the sources list file?

48 | What is the linux command to check for available disk space?

49 | What is the letter of the command in htop to search for a specific process?

50 | What is the vim command to delete the current line?

51 | What is the vim command to yank (copy) the current line?

52 | What is the linux command used to display the IP addresses of all network interfaces?

53 | What key is used to scroll up one page in a `man` page?

54 | After searching within a `man` page, what key can be used to jump to the next occurrence of the search term?

55 | What key is used to jump to the beginning of a `man` page?

### Git

56 | How many directories are there in the root directory of the `machine-learning` repository?

57 | How many total files are there in the `machine-learning` repository and all subdirectories? Not counting directories or hidden files like the `.git` repository

58 | How many python or numpy files are in the `machine-learning` repository and subdirectories?

59 | What is the short version of the commit ID of the first commit of the `machine-learning` repository?

60 | What is the long version of the commit ID of the most recent commit of the `machine-learning` repository?

61 | What city is mentioned in the 2nd most recent commit message of the `machine-learning` repository?

62 | How many branches are in the `machine-learning` repository? Don't double count references to the same branch.

63 | What is the name of the branch which isn't `main` in the `machine-learning` repository?

64 | How many different unique user addresses have pushed commits to the `machine-learning` repository?

65 | What is the name of the LICENSE of the `machine-learning` repository? Hint: it is also the full first line of the LICENSE file

66 | What is the git remote "origin" url of the seaborn repository?

67 | What is the full version of the last commit ID in the 0.12 version branch of seaborn?

The following questions concern the `master` branch of seaborn at the commit `1e6739`.

68 | How many commits are in the `master` branch of seaborn?

69 | How many tagged commits are there in the seaborn repository?

70 | How many "version" branches are there (ie, branches with a name starting in v)?

71 | What is the last item of the seaborn repository's gitignore?

72 | What is the first line of the `setup.cfg` file in the seaborn repository?

73 | How many such key fields are in the `setup.cfg` file in the seaborn repository?

74 | How many files are in the seaborn repository? Not counting hidden files like the `.git` repository

75 | How many files directly contain the word "numpy" in the seaborn repository? Do not count hidden files like `.git/`

### SSH

76 | What is the name of the Linux command used to generate SSH keys?

77 | What is the letter of the flag to specify the number of bits when generating an ssh key?

78 | What is the letter of the `ssh` flag that denotes the private key to use for authentication?

79 | What is the letter of the `ssh` flag to specify the user to log in as on the remote machine?

80 | What is the default port for `ssh`?

81 | What is the first default private key file used by `ssh`?

82 | What is the escape command to disconnect from an `ssh` pseudoterminal?

83 | What is the standard location of the per-user SSH configuration file in Linux?

84 | What is the keyword to specify the private key file in an ssh configuration file?

The following questions pertain to the remote server:

85 | How many files (excluding directories) are there in `~/`?

86 | Where are the executables accessible to the user?

87 | How many binary executables are available to the user?

88 | What is the hostname of the server?

89 | What is the kernel name of the server?

90 | What is the release of the kernel of the server?

91 | What is the MAC address of the ethernet device of the server?

92 | What is the internal IP address of the server?

93 | What is the timezone of the server?

94 | What is the remote origin URL of the git repository at `~/repo/`?

95 | What is the name of the file (without the path) that has been removed in the git repository?

96 | How many lines are in the file `~/repo/data/dogc.txt`?

97 | What is the last line of the file `~/repo/data/muni-cat.txt`?

98 | How many times does the word "biblioteca" appear in all files in `~/repo/data/`?

99 | How many `.txt` files are on the whole server?

100 | How many `.txt` files are in the home directory or its subdirectories?

### Python

Questions 101 - 120 are the responses to the exercises in the Jupyter notebook `python_intro.ipynb`, which is in the `ctf2024` github repository. Some exercises can be solved by running the code in them; try to figure them out before running the code to get the solution.

121 | What is the type of `a` in the code `a = [None] * 4`?

122 | What is the character used to start a comment in Python?

123 | True or False: `is` checks if the _value_ of two variables are the same.

124 | True or False: `==` checks if the _value_ of two variables are the same.

125 | What is the return value of the following code?

```python
a = list(range(10))
b = a[:]
b is a
```

126 | What is the return value of the following code?

```python
a = 'bonjour'
b = "bonjour"
a is b
```

127 | Which of `math.ceil` and `math.floor` gives the same result as `round` for 0.5?

128 | What is the keyword used to start a function definition?

129 | What is the name of the function used to remove whitespace in a python string?

130 | What is the type of the following code: `["a", "b", "c"]`?

131 | What is the type of the following code: `{"a", "b", "c"}`?

132 | What is the type of the following code: `"a", "b", "c"`?

133 | How many times does the following code print?

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

134 | How many times does the following code print?

```python
for i in range(10):
    if i == 4:
        continue
    print(i)
```

135 | How many times does the following code print?

```python
for i in range(10):
    if i == 4:
        pass
    print(i)
```

136 | How many times does the following code print?

```python
for n in range(2, 10):
   for x in range(2, n):
       if n % x == 0:
           break
   else:
       print(n)
```

137 | What does `http_error(402)` return in the following code?

```python
def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Bad request"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something is wrong with the internet"
```

138 | What does the following code print?

```python
def foo(arg, /):
    print(arg)

try:
    foo(arg=3)
except:
    print(4)
```

139 | What does the following code print?

```python
def foo(*, arg):
    print(arg)

try:
    foo(4)
except:
    print(3)
```

140 | What does the following code print?

```python
def foo(a, /, b, *, c):
    print(a, b, c)

try:
    foo(1, b=2, c=3)
except:
    print(3, 4, 5)
```

141 | What is the return value of the following code?

```python
from datetime import timedelta
a = timedelta(weeks=2, hours=3, seconds=32)
b = timedelta(hours=3, seconds=32, days=14, weeks=0)
a == b
```

142 | What is the first argument to the `datetime.date` function?

143 | What is the return value of the following code?

```python
import time
from datetime import date
date.today() == date.fromtimestamp(time.time())
```

144 | What is the directive used for a month's full name in `strftime`?

145 | What is the second to last element of a datetime `timetuple`?

146 | What is the result of `math.fsum([0.1]*10)`?

147 | What is the result of `sum` on the same list?

148 | What is the result of `math.isclose(math.fsum([0.1]*10), sum([0.1]*10))`?

149 | What is the python `math` function to check if a value is not a number?

150 | What is the return value of the code `math.log(1234, 10) == math.log10(1234)`?

151 | What is the return value of `math.pow(3, 0)`?

152 | What is the name of the python standard library that contains the functions `mean`, `median`, and `mode`?

153 | What is the name of the `pickle` function to write a pickled version of an object to a file?

154 | True or False: all classes that are defined inside a module can be pickled.

155 | What does the following code print?

```python
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
```

156 | What is the expected type of the first argument of `json.loads`?

157 | What does the value "null" in JSON correspond to in Python?

158 | What is the return of the following code?

```python
json.loads('{"x": 1, "x": 2, "x": 3}')
```

159 | What is the function name in the `requests` package to make an HTTP POST request?

160 | What is the name of the argument for providing an HTML payload in an HTTP POST request in the `requests` library?

## Numpy and Pandas

Questions 161 - 200 are in the numpy and pandas notebooks.

161 - 180 | numpy.ipynb

181 - 195 | pandas_titanic.ipynb

196 - 200 | pandas_air_quality.ipynb
