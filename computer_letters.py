def compteur_lettres(texte):
    d = dict(zip('abcdefghijklmnopqrstuvwxyz', (0 for i in range(len('abcdefghijklmnopqrstuvwxyz')))))
    for l in texte:
        try:
            d[l.lower()] += 1
        except:
            pass
    return d


print(compteur_lettres('Je viens d’arriver a l’Universite Libre de Bruxelles et pour l’instant je m’y plais tres bien.'))
print(compteur_lettres('Python est un langage de programmation objet, multi-paradigme et multiplateformes. Il favorise la programmation imperative structuree, fonctionnelle et orientee objet. Il est dote d’un typage dynamique fort, d’une gestion automatique de la memoire par ramasse-miettes et d’un systeme de gestion d’exceptions. Il est egalement apprecie par certains pedagogues qui y trouvent un langage ou la syntaxe, clairement separee des mecanismes de bas niveau, permet une initiation aisee aux concepts de base de la programmation.'))
