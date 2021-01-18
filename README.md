# About this
Originally, this is for testing a gacha model, which many people believe the needed gacha times for getting a 6-star character is 34. But I felt this number is quite anti-intuitive.

## [Gacha Model]
1. In first 50 times, the probality of hitting a 6-star character (the rarest rank in the pool) is 2%; 
2. After 49th gachas, each gacha that doesn't hit a 6-star character will make increase this hit probality by 2%, for example, if 50th gacha didn't hit a 6-star, then the hit probablity of 51th gacha will become 4%... if 99th were also hitting no 6-star, the hit prob of 100th will become 100%; 
3. Every time when hitting a 6-star, the hit prob will get back to 2%, and reset the next gacha as the 1st gacha.

## [About where the "34" comes from]
About this number "34", is calculated as "expected value" of this model, which is:
```python
# This is hitting probablity of Nth hitting (following the gacha model)
def current_hit_prob(Nth):
	if Nth<=50 and Nth>0:
		return 0.02
	elif Nth>50 and Nth<=100:
		return 0.02 + 0.02*(Nth-50)
	else:
		print('ERROR, an invalid input.')

# This is the probablity of event "hit at Nth gacha", which contains two parts: "in former (N-1)th gacha, you hit nothing" and "you hit 6-star at Nth"
def Prob_hit_at_Nth(Nth):
	if Nth>0 and Nth<=100:
		prob_hit_at_Nth = 1
		# "in former (N-1)th gacha, you hit nothing"
		for ith in range(1,Nth):
			prob_hit_at_Nth *= (1-current_hit_prob(ith))
		# "you hit 6-star at Nth"
		prob_hit_at_Nth *= current_hit_prob(Nth)
		return prob_hit_at_Nth
	else:
		print('ERROR, an invalid input.')


# this is the process how they get value "34"
def how_to_get_34():
	expected = 0
	sum_expected = 0
	for ith in range(1,100):
		expected += ith * Prob_hit_at_Nth(ith)
		sum_expected += Prob_hit_at_Nth(ith)
	print("total prob of hitting in 100: ", sum_expected)
	print("the expected value: ", expected)

how_to_get_34()
###(if you tried to understand the meaning of "ith", you will find very difficult to understand its mathmatic meaning.)
```

Then run this script we could get:
```sh
>>> python test.py
>>> total prob of hitting in 100:  0.9999999999999993 
the expected value:  34.59455493520977
```
If we ignore the rounding error, the first value should be 1.0.

## [People's wrong cognition]
And based on this calculation, a lot of people like to say "I have 170 gacha chances, and since the **expected gacha times for a 6-star is 34**, I might get 5 6-star characters!" I disagree with this, I believe with 170 chances, the expected 6-star should be around 3, not 5. We should use 50 as our expected time for getting a 6-star rather than 34.

## [Compare with another plain model] 
If we had a gacha model has constant 2% hitting probablity (which I call "plain model"), it is no doubt we feel the "expected times for hitting a 6-star" is 50 (1/0.02).
Then we compare this constant model with our model (which I call "relu model", since the prob curve of this model is very similar with relu activating function), we will find in the first 50 gachas, the prob model should be the SAME!

> melon-eaten-passby A: "What??? The expected value of relu model should be 34, right? Which menas I should get my 6-star at around 34 gacha, right? Why the first 50 gachas are the same as a plain model? The scientistic result is different with our intuitive conclusion! WHAT HAPPENS!!!"

## [Secert of this model]
Well, the magic trick is played on part after 50 gacha.
The relu model is like a warm-heart clerk in figure-catching-mechine, if you failed catching after 50 times, every time you failed again, she will help you move your favored figure a little so you could get it a little easier.
But the plain model is more like a cold-blood yakuza, who will do no help no matter how many times you failed.

Even in the second situation, the average of getting a 6-star is still 50 times. Now, with the help of clerk, the average value will move to less direction in no doubt.

But Never forget!!! Even this cute clerk will be warm-heart after 50 times, she is still THE SAME AS YAKUZA in former 50 times! From this opinion, the value "34" will be no reference meaning for us at all!!

## [See what's happened through simulatation experiments]
If you still didn't understand this trick, let we do a simple experiment, without any mathmatic calculation, just obvious random tests and data.

let me ask some people to gacha from 1st time in relu, then keep gaching until he/she hit a 6-star, then we record how many times she/he used; After this people's hitting, we asked next people to do the same thing, then record again.

Then we asked another group of people to do the same thing, but in plain model rather then relu model.

Here is the data we called 10,000 people * 2 groups to do this test:

![exp_result](./resource/exp_result.png)

The x-value means how many gacha they did for a 6-star, the y-value means how many people are hitting at this moment.
The deepskyblue line is for plain model, and orange line is for relu model, the limegreen line is where x=50.

We could see under plain model, there are some people who is at really really bad luck (has no hit more than gacha 400 times), while all people in relu model are hitting in 100 times.
And in former 50 times, the distribution of both model are almost the same. The ratio of hitting in former 50 times for both model are the same, which is around 63%. The peak in relu model is around 55, this is the real value we could "expect to get a 6-star", not 34 !!

## [About how to use my code]
you could check `para.py` for all avaliable parameters, my recommanded parameters are two:

1. `--num_persons`: an integer, how many people you want to test. (default=1000)
2. `--exp_type`: a string, choose from 'in_100', which ends after gacha 100 times no matter hitting or not; And 'until_hit', which ends until hitting a 6-star. (default='in_100')

PS: visualization need `amiya` support, you could get this function package in my responsity `amiya`.

```sh
>>> python main.py --num_persons=10000 --exp_type='until_hit'
>>> +++++++++++++++++++++++++
Gacha model is built:
* <prob_type>: plain
* <init_value>: 0.020000
+++++++++++++++++++++++++
Experiment parameters:
* <exp_type>: until_hit
* <num_persons>: 10000
+++++++++++++++++++++++++
+++++++++++++++++++++++++
Gacha model is built:
* <prob_type>: relu
* <init_value>: 0.020000
+++++++++++++++++++++++++
Experiment parameters:
* <exp_type>: until_hit
* <num_persons>: 10000
+++++++++++++++++++++++++
Result:
* <# of no-hit-people>: 0
* <% of no-hit>: 0.000000
* <% of hit-in-50>: 0.639600
* <average hit-#th>: 49.420500
+++++++++++++++++++++++++
Result:
* <# of no-hit-people>: 0
* <% of no-hit>: 0.000000
* <% of hit-in-50>: 0.639000
* <average hit-#th>: 34.679900
+++++++++++++++++++++++++
```

## [Conclusion]
From the experiments, we could see the relu model only help those who is at very bad luck, as for those who has "normal luck", they could hardly benefit from this.
But as long as we played this game, we eventually became at bad luck, so relu model is still better than plain model.

But! Never say "I will get a 6-star every 34 gachas on average" until you are going to gacha more than 1,000 times. And also never say "I spend 48 gacha for getting this 6-star, I am so unlucky...", since this is not true, 48 is still better than the real average value 50!

Anyway, **TAKE CARE OF GACHA GAMES! TAKE CARE OF YOUR MONEY!**


# 关于这个是干嘛的

嘛英语部分可能写的会更具体一点，中文这里就像是草稿一样，还是别看了！
para的读取和模块化的书写是个好习惯，以后要尽量习惯这种书写方式。
忘记怎么在shell里输入参数时，可以来参考这里para的写法。

大家好，我今天想和大家聊一下 **“在粥里抽到一个6星的期望是多少抽”** 这个问题。


事情大概就是这样，我们对比两种模型：
（1）爆彩概率保持0.02不变的抽卡模型
（2）当前的粥油50发之后概率增加的抽卡模型（有点像relu

前者爆彩的抽卡期望是50，后者是34。

为什么说没有参考意义呢，我们做这么一个实验：
找10,000个小朋友来，让他们从0水位开始，一直抽卡，直到爆彩为止。
然后我们比对一下大家都是在多少抽的时候爆彩的：

横坐标是“在第几抽爆彩”，纵坐标是“有多少人是在这个节点爆彩的”
深天蓝色的为模型（1）的结果，橙色的为模型（2）的结果。
比对一下不难发现，2者在50抽之前的“爆彩”这一事件分布是完全相同的！
也就是说，如果你抽不到50发，模型（1）还是（2）对你来说都是没有任何区别的




为什么我会想来讨论已经被聊烂的问题呢，是针对一些类似这样的发言：

> "草，6星的期望是34抽，你这都54了还不出，也太非了吧！"
纠正：54抽不出6，绝对算是正常范围，最多算“不欧”

> "34抽的6星期望，我准备160抽，70%的up率，总不可能5个6星全给我歪了吧！"
纠正：160抽的期望绝对不够5个六星，-应该是170（不是-，想要出5个六星，要准备的抽数应该在170以上



我的观点是：34抽一个六星在统计上是绝对成立的，但是34这个数字对于一个“普通粥油玩家”来说，没有任何的参考意义。



首先我们说说关于这个“34”的期望值，是怎么算出来的。

这个34，是“在粥油抽卡模型下，从0开始直到抽到1一个六星为止”这一事件的“数学期望”，也就是“平均下来需要多少抽”。
直观的解释是什么意思呢？我抽出第一个六星用了10抽，小明抽出第一个六星用了40抽，我们平均一下就是“抽出一个六星平均需要25抽”。然后我们把人数扩大，有10000个人，把所有人抽到6星用的次数加起来，再除以我们的总人数，得到的平均数，就是34所代表的“数学期望”的意思。

具体的计算过程，很多很多人都写文章解释过了，我也没必要再写一遍。

但是数学期望是34的意义，并不代表当我抽到第34发的时候，我的内心就可以小激动：“哇我摸到期望了，接下来马上就要出了，我可以小期待一下啦～！”的这种“期望”，而是一个冰冷的数学概念。对于一个普通玩家来说，这种“情感期望”的数值应该是50。


