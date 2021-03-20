API ALERTS PROGRAMMING CHALLENGE

- No Necessary instructions are needed. I tested this in Command Prompt.

- Must have the proper libraries installed (requests, json, sys, datetime, statistics)
	- input example is as follows

	python apiAlerts.py -c btcusd -t ALL

- If I had more time to improve (which I probably will in my own time), I would clean up the
  code a little more and implement a better way to deal with the command line arguements
  so things such as -h would bring up a proper help menu.

- Other interesting checks would be to look at the amount of money that sellers have made for a particular crypto
  For example, in the past 24 hours, BTC sellers made X amount of money. 
  Another good one would be to determine whether the crypto is volatile or stable, however this would require
  a larger data set.

- The only issues I faced were to find the right API to call. Even using ctrl+f I had some difficulty
  finding what I wanted.

- It took me ~ 2.5 hours to complete this challenge
    - 30 minutes to read documentation
    - 15 minutes to mess around with API
    - 30 minutes to write Standard Deviation Function 
    - 15 minutes to write the Price Change Function
    - 30 minutes to write the Volume Deviation Function
    - 30 minutes to handle the CLI args and assorted cases (currency missing, wrong function, etc)
        - Totals to 2.5 hours

- In closing, I just want to say how much I enjoyed this assignment. It varies greatly from other
  companies and I value that. It was fun, thought-provoking and taught me about a new API I have never used before.
  So, thank you.

~~ Jon Cucci
