def default_search(my_reasearch, my_max):
	my_liste_2_recherche = list(range(my_max))
	count = 0
	if (my_reasearch in my_liste_2_recherche) :
		for x in my_liste_2_recherche :
			if x == my_reasearch :
				print('Lineraire(): nombre iteration :' + str(count))
				return True
			else:
				count += 1
				next
	else :
		return False


def dicho(my_reasearch, my_list, count) :
	my_liste_2_recherche = my_list
	my_max = len(my_liste_2_recherche)
	
	if (my_reasearch in my_liste_2_recherche) :
		my_liste_center = len(my_liste_2_recherche) // 2
		
		if ( my_reasearch == my_liste_2_recherche[my_liste_center]):
			count = count + 1
			print('dicho() :: nombre iteration :' + str(count))
			return my_liste_2_recherche[my_liste_center]

		if ( my_reasearch > my_liste_2_recherche[my_liste_center]):
			my_liste_2_recherche = my_liste_2_recherche[my_liste_center : my_max]
			count = count + 1
			return dicho(my_reasearch, my_liste_2_recherche, count)
		
		if ( my_reasearch < my_liste_2_recherche[my_liste_center]):
			my_liste_2_recherche = my_liste_2_recherche[0: my_liste_center]
			count = count + 1
			return dicho(my_reasearch, my_liste_2_recherche, count)

	else :
		return False