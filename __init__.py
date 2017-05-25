# -*- coding: utf-8 -*-
import random;

global CMD;
CMD=['dc', 'sl', 'fjp', 'hcp', 'bhq','ssjp', 'ssws'];
global WSSS;
WSSS=0;

def onQQMessage(bot, contact, member, content):
	if contact.ctype=='group' and contact.qq=='572661635':
		draw(bot, contact, member, content);

def draw(bot, contact, member, cmd):
	global CMD;
	if cmd in CMD:
		if cmd=='dc':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+dc(),resendOn1202=False);
		elif cmd=='sl':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+sl(),resendOn1202=False);
		elif cmd=='fjp':
			bot.SendTo(contact,'@'+member.name+'的'+cmd+'结果：\n'+fjp(),resendOn1202=False);
		elif cmd=='hcp':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+hcp(),resendOn1202=False);
		elif cmd=='bhq':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+dc(),resendOn1202=False);
		elif cmd=='ssjp':
			bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+ssjp(),resendOn1202=False);
		elif cmd=='ssws':
			ssws();

def dc():
	global WSSS;
	prob=random.randint(0, 100);
	if WSSS>0:
		if prob<10:
			result='UR';
		elif prob<30:
			result='SSR';
		elif prob<60:
			result='SR';
		else:
			result='R';
		WSSS-=1;
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
	global WSSS;
	prob=random.randint(0, 100);
	if WSSS>0:
		if prob<50:
			result='UR';
		else:
			result='SR';
		WSSS-=1;
	else:
		if prob<20:
			result='UR';
		else:
			result='SR';
	return result;

def hcp():
	global WSSS;
	prob=random.randint(0, 100);
	if WSSS>0:
		if prob<30:
			result='UR';
		elif prob<60:
			result='SSR';
		else:
			result='SR';
		WSSS-=1;
	else:
		if prob<10:
			result='UR';
		elif prob<30:
			result='SSR';
		else:
			result='SR';
	return result;

def ssjp():
	global WSSS;
	prob=random.randint(0, 100);
	if WSSS>0:
		if prob<30:
			result='UR';
		elif prob<60:
			result='SR';
		else:
			result='R';
		WSSS-=1;
	else:
		if prob<10:
			result='UR';
		elif prob<40:
			result='SR';
		else:
			result='R';
	return result;

def ssws():
	global WSSS;
	WSSS=random.randint(1, 55);
