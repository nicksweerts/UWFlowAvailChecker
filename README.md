# UWFlowAvailChecker
Checks the availability of classes on UWFlow every 30 seconds and then sends an email if there are changes.

Use SystemCtl to have this run as a process in the background on a raspberry pi and you will be updated each time that there are changes in the number of students enrolled in the class. This allows you to grab the spot before anyone else gets notified by UWFlow (only happens every 30 mins).
