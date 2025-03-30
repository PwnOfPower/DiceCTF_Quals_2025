# Dicecap


Description:

```
As DiceGang haven't won a CTF in 4 months, we've taken to more drastic measures 
to get to the top of the leaderboard - hacking our competitors! 
This pcap was gathered from a previous ``information gathering`` mission, can you find the flag?
```


Doing a `$ strings challenge.pcap | grep -i flag`

We saw a `flag.txt` file

Taking a look at the PCAP file I saw many FTP packages, so I clicked on `Follow TCP Stream`

And it export me the nexto file:


```
220 (vsFTPd 3.0.5)
USER hacker
331 Please specify the password.
PASS hacker
230 Login successful.
SYST
215 UNIX Type: L8
FEAT
211-Features:
 EPRT
 EPSV
 MDTM
 PASV
 REST STREAM
 SIZE
 TVFS
211 End
EPSV
229 Entering Extended Passive Mode (|||19850|)
LIST
150 Here comes the directory listing.
226 Directory send OK.
EPSV
229 Entering Extended Passive Mode (|||20104|)
NLST
150 Here comes the directory listing.
226 Directory send OK.
CWD sekrit-encryptor
250 Directory successfully changed.
TYPE I
200 Switching to Binary mode.
SIZE main
213 16296
EPSV
229 Entering Extended Passive Mode (|||10486|)
RETR main
150 Opening BINARY mode data connection for main (16296 bytes).
226 Transfer complete.
MDTM main
213 20250327234415
CWD ..
250 Directory successfully changed.
TYPE A
200 Switching to ASCII mode.
EPSV
229 Entering Extended Passive Mode (|||44361|)
LIST
150 Here comes the directory listing.
226 Directory send OK.
EPSV
229 Entering Extended Passive Mode (|||11398|)
NLST
150 Here comes the directory listing.
226 Directory send OK.
CWD super_skiddy_tools
250 Directory successfully changed.
EPSV
229 Entering Extended Passive Mode (|||47697|)
NLST
150 Here comes the directory listing.
226 Directory send OK.
TYPE I
200 Switching to Binary mode.
SIZE coolzip.zip
213 1170
EPSV
229 Entering Extended Passive Mode (|||33937|)
RETR coolzip.zip
150 Opening BINARY mode data connection for coolzip.zip (1170 bytes).
226 Transfer complete.
MDTM coolzip.zip
213 20250328014837
```

Searching `ftp-data` I found the `coolzip.zip` so I download it by:
`File` > `Export Objects` > `FTP-DATA`.

The `.zip` is password protected.


There is another binary called `main`, when you run it, the output is:

```
The password is:1743367680LC_CTuser
```


When you see the assembly code, you see the output is splitted in three parts:
```
<timestamp><locale><user>.
```

So we develop a python script to bruteforce the possible combinations.

```python
import time

# Define the range
start_timestamp = 1740000000  # Updated timestamp range
end_timestamp = int(time.time())  # Current timestamp

# Possible locales (updated list)
locales = ["LC_CT", "LC_ALL", "en_US"]
username = "hacker"

# Output file
output_file = "password_list.txt"

with open(output_file, "w") as f:
    for timestamp in range(start_timestamp, end_timestamp + 1): 
        #seconds_mod_60 = timestamp % 60
        for locale in locales:
            password = f"{timestamp}{locale}{username}\n"
            f.write(password)

print(f"Password list generated: {output_file}")

```

Generate the `password_list.txt` by running the script and run `john` by:

```bash
$ ~/github/john/run/john  --wordlist=password_list.txt  hashes.txt
```

AndyYou get the password to unzip the file and get the flag.

```bash
$ ~/github/john/run/john  --show hashes.txt 
coolzip.zip/flag.txt:1743126480en_UShacker:flag.txt:coolzip.zip:coolzip.zip
```

```bash
$ cat flag.txt
dice{5k1d_y0ur_w@y_t0_v1ct0ry_t0d4y!!!}
```
