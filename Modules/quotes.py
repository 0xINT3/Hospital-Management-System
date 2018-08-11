import random
quote = ['"If you don\'t think healthcare is about power, you haven\'t been paying attention."', '"You don\'t appreciate life until you get to the other side. Like lying in a hospital bed."','"Wherever the art of medicine is loved, there is also a love of humanity."','"Healing in a matter of time, but it is sometimes also a matter of opportunity."','"Cure sometimes, treat often, comfort always."','"The hospital industry to this day works its tail off to do the right thing."','"The most frequent lie in a hospital: it won\'t hurt."']
def display():
    x = random.randint(0,6)
    return ("Quote of the day: " + quote[x])
