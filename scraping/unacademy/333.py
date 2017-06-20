from __future__ import unicode_literals
# from bs4 import BeautifulSoup
# import urllib2
# import re
import unicodecsv as csv
import ast

words1 = {
	'homogenous' 	: 'of the same kind, alike',
	'anomalous'		: 'abnormal. irregular',
	'paragon'		: 'model of perfection',
	'precursor'		: 'predecessor, forerunner',
	'inchoate'		: 'recently begun, rudimentary',
	'intractable'  	: 'hard to control and manage',
	'perennial' 	: 'enduring, continually recurring',
	'mitigate'		: 'appease, moderate',
	'aesthetic'		:	'principles underlying the work of an artist, dealing with beauty',
	'luminous'		: 'giving off light',
	'magnanimity' 	: 'kindness in giving, generosity',
	'inundate'		: 'overwhelm',
	'salubrious' 	: 'healthful, benefecial',
}

words2 = {
	'ostentatious' 	: 'pverdone, pretentious, tacky display',
	'distend' 		: 'swell due to pressure from inside, swell, expand',
	'approbation' 	: 'approval',
	'implode' 		: 'burst inwards',
	'bombastic' 	: 'high sounding with little meaning',
	'grandeloqious' : 'pmpous in style or language',
	'felicitious' 	: 'lucky, suited to the situation',
	'morose' 		: 'gloomy, melancholy',
	'fervor' 		: 'intense and passionate feeling',
	'opprobrium' 	: 'public disgrace, infamy, high criticism',
	'perfunctory' 	: 'superficial, not thorough',
	'mollify' 		: 'soothe',
	'enhance' 		: 'intensify, improve the quality of',
	'satiate' 		: 'supply with excess, supply'
}

words3 = {
	'implacable' 	: 'not capable of being appeased',
	'alleviate' 	: 'relieve, make less intense',
	'anarchy' 		: 'state of disorder due to absence of governing body',
	'aggregate' 	: 'to collect, gather into a mass',
	'relegated' 	: 'demote, banish to an inferior position',
	'onerous' 		: 'burdensome, oppressive',
	'irresolute' 	: 'uncertain how to act, indecisive',
	'pragmatic' 	: 'practical (as opposed to idealistic)',
	'diatribe' 		: 'abusive speech or piece of writing',
	'harangue' 		: 'loud and aggressive speech, verbal attack',
	'abeyance' 		: 'state of temporary disuse',
	'pedantic' 		: 'showing off learning, giving too much importance to details and formal rules'
}

words4 = {
	'elegy' 		: 'a serious and sad poem displaying grief or mourning',
	'dirge' 		: 'mournful piece of music, a literary or musical lament',
	'coda'			: 'concluding section of a dance or piece of music',
	'stolidly' 		: 'calm, dependable, showing little emotion',
	'prevaricate' 	: 'speak or act in an evasive way',
	'platitude' 	: 'overused remark or statement which is no longer interesting and thoughtful',
	'pathological' 	: 'involving or caused by a disease OR excessive level of some quality',
	'immutable' 	: 'fixed, unchanging over time',
	'quiescent' 	: 'quiet, in a state or period of inactivity',
	'condone'		: 'accept and approve something BUT with reluctance',
	'beneficent' 	: 'prone to doing kind and generous things',
	'placate' 		: 'appease, relieve',
	'ambiguous'		: 'open to more than one meaning'
}

words5 = {
	'pervasive'		: 'spreading widely',
	'dormant' 		: 'temporarily inactive',
	'equanimity' 	: 'calmness and composure esp. in a diff situation',
	'resolve' 		: 'determination, firmness of purpose',
	'emulate' 		: 'immitate or match',
	'deference' 	: 'polite submission and respect',
	'viable' 		: 'practical, workable, feasible',
	'assuage' 		: 'ease or lessen pain',
	'invective' 	: 'abusive language to criticize',
	'tirade' 		: 'long angry speech, harangue',
	'eulogy' 		: 'expression of praise on occassion of death',
	'ebullient' 	: 'full of energy',
	'exacerbate' 	: 'to make a situation worse' 
}

words6 = {
	'plethora' 		: 'large amount (excessive variety)',
	'abstemious' 	: 'holding back from indulgence',
	'connoisseur' 	: 'expert in a particular subject',
	'antipathy' 	: 'deep feeling of dislike',
	'alacrity' 		: 'cheerful readiness',
	'appropriate' 	: '(v.) take something for one\'s own use, usually without permission OR devote money fpr a special purpose (allocate funds)',
	'desiccate' 	: 'dried up, without moisture',
	'admonished' 	: 'scold and warn (out of care)',
	'dissolution' 	: 'formally ending a partnership OR living a life of indulgence in sensual pleasures',
	'burnish' 		: 'to polish, make shiny',
	'conciliatory' 	: 'trying to regain friendship or goodwill',
	'obsequieous' 	: 'excessively submissive, overly obedient',
	'savor' 		: 'enjoy something to the full'
}

words7 = {
	'efficacy' 		: 'ability to produce a desired result',
	'disseminate' 	: 'tp spread (esp. information)',
	'verbose' 		: 'using an excessive amount of words',
	'complaisant' 	: 'inclination to oblige others',
	'irascible' 	: 'tendency to be easily annoyed',
	'tractable' 	: 'easy to control or influence',
	'compliant' 	: 'in accordance with rules or standards',
	'reproach' 		: '(n.) expression of disapproval, (v.) to express disapproval or disappointment',
	'refractory' 	: 'stubborn and hard to manage',
	'transgression' : 'violation of duty, law or moral principle',
	'capricious' 	: 'fickle, unpredictable mood',
	'reticent' 		: 'not revealing one\'s feelings',
	'guile' 		: 'carfty or artful deception esp. in attaining a goal, insidious and cunning',
	'soporific' 	: 'tending to cause drowsiness or sleep'
}

words8 = {
	'inadvertently' : 'accidental, resulting from carelessness',
	'mendacious' 	: 'lying, dishonest',
	'reprobate' 	: 'unrpincipled person',
	'impeding' 		: 'preventing or interfering with the progress of something',
	'caustic' 		: 'exteremely sarcastic or critical',
	'vituperative' 	: 'bitter, harsh, abusive',
	'castigation' 	: 'harsh, verbal scolding',
	'boorish' 		: 'rude, insensitive, bad mannered person',
	'contrite' 		: 'show remorse, feel guilty',
	'wary' 			: 'showing caution about danger',
	'chicanery' 	: 'trickery and decption',
	'appease' 		: 'pacify someone by meeting their demands',
	'warranted' 	: 'justified, necessary, needed',
	'audacious' 	: 'recklessly bold and daring (can be +ve or -ve)'
}

words9 = {
	'indolent' 		: 'lazy, wanting to avoid activity',
	'strut' 		: '(v.) walk pompously with attitude',
	'pristine' 		: 'pure, clean and spotless',
	'levee' 		: 'embankment to prevent overflow of river an flooding',
	'torpor' 		: 'state of being motionless (emotional or physical)',
	'gregarious' 	: 'sociable, fond of company',
	'lethargic' 	: 'sluggish, dull, inactive',
	'abscond' 		: 'leave secretky and hide',
	'officious' 	: 'assertive of authority, offensively interfering, intrusive with help or advice',
	'assiduous' 	: 'showing great care and effort',
	'plasticity' 	: 'quality of being reshaped and molded',
	'porous' 		: 'having minute holes',
	'whimsically' 	: 'in an amusing or playful manner',
	'tortuous' 		: 'full of twists and turns, lengthy'
}

words10 = {
	'arduous' 		: 'demanding great effort',
	'confound' 		: 'to cause surprise/confusion OR to mix up',
	'austere' 		: 'having no luxury (plain and without decoration) OR strict',
	'probity' 		: 'having strong moral principles, integrity',
	'inconsequential' : 'not important or significant',
	'mundane' 		: 'lacking excitement, found in ordinary course of events',
	'belie' 		: 'to contradict OR to give a false impression of something',
	'skeptic' 		: 'person who questions accepted opinions',
	'fledgling' 	: 'person or group that is inexperienced',
	'sage' 			: '(n.) a person known for wisdom, (adj.) wise',
	'profound' 		: 'deep, intense or great OR having good knowledge',
	'desultory' 	: 'not having any plan, occuring sporadically',
	'recluse' 		: 'a person who lives a solitary life (avoids company)',
}

words11 = {
	'spectrum' : 'a broad range of values',
	'eclectic' : 'derived from various sources and styles',
	'disparate' : 'not allowing comparison',
	'strut' : '(n.) a strong rod or bar of metal/wood that holds a vehicle or building together (framework)',
	'buttress' : '(n.,v.) structure that provides strength and support',
	'garrulous' : 'overly talkative, mosty about unimportant things',
	'fatuous' : 'silly and pointless, stupid, lacking intelligence',
	'banal' : 'obvious and boring, lacking originality',
	'gullible' : 'easily convinced or fooled',
	'gouge' : 'overcharge or deceive',
	'dupe' : '(n.) someone who is easily fooled (v.) to trick or deceive',
	'apathy' : 'lack of concern and interest'
}

words12 = {
	'abate' : 'reduce in intensity',
	'logs' : 'written record of an event',
	'loquacious' : 'very talkative',
	'delineate' : 'clearly describe something, indicate the exact boundary of an area',
	'contentious' : 'controversial, likely to cause an argument',
	'craven' : 'overly cowardly',
	'endemic' : 'native to a specific area or group of people',
	'stipulate' : 'demand something as a part of contract',
	'default' : 'fail to satisfy a commitment',
	'discordant' : 'in disagreement',
	'flout' : 'openly disobey a rule or law',
	'effrontery' : 'shamelessly bold behaviour',
	'foment' : 'to incite or stir up',
}

words13 = {
	'futile' : 'pointless',
	'facetious' : 'not being serious about a serious subject',
	'artless' : 'without deception i.e. innocent and simple',
	'intransigence' : 'stubborn and uncompromising',
	'denigrated' : 'criticize unfairly',
	'deride' : 'ridicule bitterly',
	'truculence' : 'ferociousness, eagerness to fight',
	'penury' : 'state of extreme poverty',
	'insipid' : 'tasteless',
	'pungent' : 'intense smell or taste',
	'occluded' : 'blocked',
	'aberrant' : 'deviating from original plan'
}

words14 = {
	'diffident' : 'modest and shy due to lack of self-confidence',
	'supersede' : 'to replace something',
	'imperturbable' : 'unable to get excited, calm',
	'apprise' : 'to report on the status of something',
	'decorum' : 'proper behaviour',
	'commensurate' : 'in proportion, equal',
	'daunt' : 'make someone feel intimidated or scared',
	'meticulous' : 'showing great attention to detail',
	'convoluted' : 'extremely complex',
	'vacillate' : 'waver between decisions, undecided',
	'adulterate' : 'to make something impure by addition of something else',
	'distill' : 'purify and extract essence of',
	'goad' : 'annoy and provoke to get a reaction',
	'presumptuous' : 'making a judgement before knowing all of the facts',
}

words15 = {
	'welter' : 'a confused jumble, wild disorder',
	'fawning' : 'giving a lot of attention in a flattering manner',
	'idolatry' : 'extreme devotion and admiration',
	'propriety' : 'following what is socially acceptable in speech and behaviour',
	'prodigal' : 'spending resources wastefully and freely',
	'propitiate' : 'win the favour of someone by doing something',
	'disparage' : 'to express a negative opinion',
	'frugal' : 'careful in spending money',
	'stint' : '(v.) supply an inadequate amount of something, to restrict in a stingy manner',
	'rarefied' : 'relevant to a very small group',
	'digression' : 'temporary deviation from main topic',
	'malingerer' : 'someone who pretends to be sick to avoid work',
	'reverent' : 'showing immense respect',
	'solicitous' : 'full of interest, anxiety and concern'
}

words16 = {
	'erudite' : 'having or showing profound knowledge',
	'tacit' : 'implied but not directly stated',
	'neophyte' : 'someone who is new to something',
	'exigency' : 'pressing and necessary',
	'fallacious' : 'idea or belief that is false',
	'dismiss' : 'disregard and treat as unworthy of consideration',
	'burgeon' : 'to grow and expand',
	'forestall' : 'to stop something from happening',
	'impermeable' : 'to not allowing passage',
	'obviate' : 'to prevent or eliminate',
	'analagous' : 'similar',
	'gainsay' : 'to contradict or deny',
	'problematic' : 'constituting or presenting a problem',
	'ascetic' : 'leading a life of self-denial and self-discipline'
}

words17 = {
	'indeterminate' : 'not fixed or known',
	'cogent' : 'very clear and convincing',
	'impassive' : 'revealing little emotion, expressionless',
	'prohibitive' : 'tending to prohibit, disallow',
	'lassitude' : 'tiredness and lack of energy',
	'inert' : 'without power to act or move',
	'diffuse' : 'very wordy, lacking clarity or conciseness',
	'resolution' : 'determination',
	'penchant' : 'a strong liking for',
	'itinerary' : 'a planned route or journey',
	'tenuous' : 'weak and likely to change',
	'subside' : 'become less intense and violent',
	'recant' : 'rescind, to retract a public statement',
	'repudiate' : 'to reject and refuse to support',
	'saturate' : 'fill to the utmost capacity'
}

words18 = {
	'recalcitrant' : 'stubborn and resistant to authority',
	'specious' : 'seems to be true but is actually false',
	'incongruous' : 'incompatible',
	'shard' : 'a sharp piece of glass or pottery',
	'impair' : 'weaken or damage',
	'flag' : 'become tired and weaker (in spirit and confidence)',
	'innocuous': 'harmless and innocent',
	'plummet' : 'fall down or drop down at high speed',
	'attenuate' : 'to reduce, weaken',
	'precarious' : 'dangerously likely to fall or collapse',
	'bolster' : 'to makse something more strong and bold, support',
	'striated' : 'striped',
	'viscous' : 'thick and slow to move',
	'coagulate' : 'to thicken or develop into a mass'
}

words19 = {
	'insensible' : 'unresponsive and unconscious',
	'malleable' : 'easily impressionable',
	'implicit': 'indirectly suggested',
	'discredit': 'dsibelieve, harm the reputation of, defame',
	'laconic': 'to the point and direct, not verbose',
	'elicit': 'evoke or draw out',
	'dissembling': 'disguise, hide behind a false appearance',
	'levity': 'lack of seriousness, frivolous',
	'lucid': 'clear to understand'
}

words20 = {
	'converge' : 'to come together',
	'derivative' : 'unoriginal and derived from something else',
	'indigence' : 'extreme poverty',
	'paucity' : 'scarcity',
	'discrepancy' : 'lack of consistency',
	'supposition' : 'belief without proof, hypothesis',
	'ingenuous' : 'gullible, naive and innocent',
	'insularity' : 'narrow mindedness, isolation (parochial, partisan)',
	'dichotomy' : 'branching into tow contradictory paths',
	'embellish' : 'enhance, decorate'
}

words21 = {
	'autonomous' : 'having its own governing system, independent',
	'dogmatic' : 'opinionated, believing one\'s principles are true', 
	'iconoclast' : 'someone who attacks cherished traditions',
	'inherent' : 'established by nature or habit',
	'quibble' : 'minor objection or complaint',
	'venerate' : 'revere, regard with respect',
	'proscribe' : 'forbid, especially by law',
	'diverge' : 'going in different direction (opp. of converge)',
	'discrete' : 'consisting different parts, separate',
	'laud' : 'praise highly'
}

words22 = {
	'disabuse' : 'to correct a false impression',
	'misanthrope' : 'one who dislikes mankind',
	'aver' : 'declare, state formally',
	'preopensity' : 'natural inclination',
	'equivocate' : 'mislead, attempt to conceal the truth',
	'sporadic' : 'occurring irregularly', 
	'phlegmatic' : 'having a calm disposition',
	'exculpate' : 'free from blame',
	'piety' : 'the quality of being religious',
	'insinuate' : 'hint at, imply an accusation',
}

words23 = {
	'volatile' : 'liable to change unpredictably',
	'substantiate' : 'establish by evidence, prove',
	'contention' : 'claim, assert, thesis ()',
	'esoteric' : 'known to only a few',
	'recondite' : 'little known, hard to understand',
	'compendium' : 'collection of facts, comprehensive summary',
	'document' : '(v.) provide written evidence',
	'sanction' : 'approve or ratify by governing body',
	'deterrant' : 'something that discourages action, obstacle',
	'hyperbole' : 'exaggeration',
	'perfidious': 'deceitful, treacherous',
	'precipitate' : '(adj.) hasty, sudden (v.) cause to happen suddenly'
}

words24 = {
	'enervate' : 'weaken, reduce force or strength',
	'conundrum' : 'puzzle, problem',
	'partisan' : 'prejudiced, favoring a cause',
	'ambivalence' : 'having contradictory or confused emotions',
	'disingenuous' : 'insincere',
	'oscillate' : 'move back and forth',
	'disinterested' : 'impartial',
	'discerning' : 'having an insight, quick and observant',
	'tangential' : 'deviating from a path,  irrelevant',
	'subpoena' : 'a legal document which summons a person to court'
}

words25 = {
	'qualify' : 'limit, restrict, add conditions, refine',
	'facillitate' : 'make something easier',
	'ameliorate' : 'improve, make something better',
	'divest' : 'strip something of, deprive',
	'rescind' : 'to cancel (especially a law)',
	'amalgamate' : 'joing together into one',
	'permeable' : 'porous',
	'incorporate' : 'to combine and make larger',
	'engender' : 'cause to produce/happen',
	'latent' : 'hidden but has potential',
	'impervious' : 'immune to damage',
}

words26 = {
	'maverick' : 'nonconformist, someone who rebels (Elon Musk)',
	'metamorphosis' : 'transformation',
	'proliferated' : 'multiply and grow rapidly',
	'preamble' : 'introductory statement',
	'empirical' : 'based on observation and experience rather than theory',
	'anachronism' : 'misplaced in time',
	'catalyst' : 'an agent that speeds up an action',
	'obdurate' : 'stubborn, hardhearted',
	'ephemeral' : 'short-lived and fleeting',
	'disjointed' : 'lacking coherence'
}

# dicts = [('words' + str(x)) for x in range(1,27)]
# final_dict = {}
# for item in dicts:
# 	final_dict.update(item)

for i in range(1,27):
	with open('333unacademy'+str(i)+'.csv','wb') as f:
	    w = csv.writer(f)
	    dict_name = eval('words'+str(i))
	    w.writerow(['WORDS'+str(i),''])
	    # w.writerow(['Name','Meaning'])
	    c = 0
	    for k,v in dict_name.iteritems():
		    try:
		    	w.writerow([k,v])
		    	c+=1
		    except UnicodeEncodeError:
		    	pass
		    	print "Unicode exception!"
		#w.writerow([])
		# print "Words added to CSV"+str(i)": ",c


with open("final333list.csv","a") as fout:
	for num in range(1,27):
		for line in open("333unacademy"+str(num)+".csv"):
			fout.write(line)












