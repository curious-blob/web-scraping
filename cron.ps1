$action = "python3 cron.py"
$trigger = New-JobTrigger -Once -At 9:00AM -RepetitionInterval (New-TimeSpan -Hours 12) -RepeatIndefinitely
$options = New-ScheduledJobOption -RunElevated -RequireNetwork

Register-ScheduledJob -Name Scrape-Dataset -Trigger $trigger -ScriptBlock $action -MaxResultCount 5 -ScheduledJobOption $options