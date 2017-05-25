# -*- coding: utf-8 -*-
import random;

CMD=['dc', 'sl', 'fjp', 'hcp'];
wsss=0;

def onQQMessage(bot, contact, member, content):
	if contact.ctype=='group' and contact.qq=='572661635':
		draw(bot, contact, member, content);

def draw(bot, contact, member, cmd):
	if cmd in CMD:
		if cmd=='dc':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+dc());
		elif cmd=='sl':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+sl());
		elif cmd=='fjp':
			bot.SendTo(contact,'@'+member.name+'的'+cmd+'结果：\n'+fjp());
		elif cmd=='hcp':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+hcp());
		elif cmd=='ssjp':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+ssjp());
		elif cmd=='ssws':
			ssws();

def dc():
	prob=random.randint(0, 100);
	if wsss>0:
		if prob<10:
			result='UR';
		elif prob<30:
			result='SSR';
		elif prob<60:
			result='SR';
		else:
			result='R';
		wsss-=1;
	else:
		if prob<1:
			result='UR';
		elif prob<5:
			result='SSR';
		elif prob<20:
			result='SR';
		else:
			result='R';
	return result;

def sl():
	res={'UR':0, 'SSR':0, 'SR':0, 'R':0};
	result='';
	for i in range(11):
		res[dc()]+=1;
	result='UR=%d  SSR=%d  SR=%d  R=%d'%(res['UR'], res['SSR'],res['SR'], res['R']); 
	return result;

def fjp():
	prob=random.randint(0, 100);
	if wsss>0:
		if prob<50:
			result='UR';
		else:
			result='SR';
		wsss-=1;
	else:
		if prob<20:
			result='UR';
		else:
			result='SR';
	return result;

def hcp():
	prob=random.randint(0, 100);
	if wsss>0:
		if prob<30:
			result='UR';
		elif prob<60:
			result='SSR';
		else:
			result='SR';
		wsss-=1;
	else:
		if prob<10:
			result='UR';
		elif prob<30:
			result='SSR';
		else:
			result='SR';
	return result;

def ssjp():
	prob=random.randint(0, 100);
	if wsss>0:
		if prob<30:
			result='UR';
		elif prob<60:
			result='SR';
		else:
			result='R';
		wsss-=1;
	else:
		if prob<10:
			result='UR';
		elif prob<40:
			result='SR';
		else:
			result='R';
	return result;

def ssws():
	wsss=random.randint(1, 55);
