def computador_escolhe_jogada(n, m):
	
	i = 1
	x = 0

	while (m + 1) * i < n:
		x = (m + 1) * i
		i = i + 1

	if n - x >= m:
		p = m

	else:
		p = n - x

	return p