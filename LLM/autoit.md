

Func LoopFlagToggle()
    $loopflag = 1
EndFunc

HotKeySet("{esc}","LoopFlagToggle")
HotKeySet("{s}","LoopFlagToggle")
$loopflag = 0

$x = 1279
$y = 677
$offsetx = 12
$offsety = 12


While $loopflag = 0
	MouseMove(Random($x-$offsetx, $x+$offsetx), Random($y-$offsety, $y+$offsety), Random(3,12))
	MouseClick("left", 1279, 677, Random(1,2), Random(5,10))
	Sleep(Random(10000,30000))
	Send("a")
	MouseMove(Random(1000, 1010), Random(500, 510), Random(3,12))
	Sleep(Random(30000,60000))
WEnd
You'll need to download autoit to run it, then just save it as an .au3 file or use the SciTE-Lite editor that comes with autoit to edit it.

Atm it moves the mouse to a random point within 12 pixels of x=1279 and y=677 on your screen, clicks and tries to type an 'a'. SO just change that to a place on your screen where it'll click Colab but not anything important. I got it t click a text cell and type in that. I don't think the typing's actually necessary but I added it just in case.

You can see the coordinates of your mouse by opening the autoit window info app that comes with autoit. I got all this from this video, which was super helpful: https://www.youtube.com/watch?v=xIT1KUSllNs