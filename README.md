# About this
Originally, this is for testing a gacha model, which many people believe the needed gacha times for getting a 6-star character is 34. But I felt this number is quite anti-intuitive.

> [Gacha Model]
> (1) In first 50 times, the probality of hitting a 6-star character (the rarest rank in the pool) is 2%; 
> (2) After 49th gachas, each gacha that doesn't hit a 6-star character will make increase this hit probality by 2%, for example, if 50th gacha didn't hit a 6-star, then the hit probablity of 51th gacha will become 4%... if 99th were also hitting no 6-star, the hit prob of 100th will become 100%; 
> (3) Every time when hitting a 6-star, the hit prob will get back to 2%, and reset the next gacha as the 1st gacha.

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
``` 



People like to say "I have 170 gacha chances, and since the **expected gacha times for a 6-star is 34**, I might get 5 6-star characters!" I disagree with this, I believe with 170 chances, the expected 6-star should be around 3, not 5. We should use 50 as our expected time for getting a 6-star rather than 34.




# 关于这个是干嘛的
 
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


