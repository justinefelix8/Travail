#Importer streamlit, matplotlib, pandas et numpy
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Entête du site/Présentation de la plateforme
st.set_page_config(page_title="Êtes-vous prêt pour votre retraite ?", layout="wide")

st.title(f"Êtes-vous prêt pour votre retraite ?")

st.write(f"La retraite est un aspect très important lorsque vient le temps de faire une bonne planification financière. Habituellement, l'âge de retraite au Québec est de 65 ans. Il est primordial de bien connaître ses capacités financières en effectuant une analyse de budget afin de déterminer les montants disponibles pour l'épargne. Ainsi, il est possible de s'assurer d'avoir les économies suffisantes lorsqu'il viendra le temps de prendre sa retraite, pour veillir en toute tranquilité !" )

st.write(f"Notre plateforme en ligne vous permettera de répondre à une question importante. :blue[**_Êtes-vous prêt pour votre retraite ?_**]")

st.write(f"Présenté par Félix Pouliot et Justine Pelletier")

#Division du site en trois volets
tab1, tab2, tab3 = st.tabs(["Budget", "Retraite", "Analyse"])

#Premier volet - Buget
with tab1:

    st.title(":blue[Budget]\n")

    #Valeurs à indiquer afin d'analyser le budget
    salaire = st.number_input("Quel est votre salaire annuel ?", value = 50000.0)

    habitation = st.number_input("Quel est le montant mensuel accordé pour votre loyer et/ou hypothèque ?", value = 1000.0)

    alimentation = st.number_input("Quel est le montant menseul accordé pour vos repas ?", value = 500.0)

    utilité = st.number_input("Quel est le montant mensuel accordé pour les besoins autres (cellulaire, assurances, abonnement) ?", value = 200.0)

    transport = st.number_input("Quel est le montant mensuel accordé pour vos déplacements (prêt auto, essence, transports en commun) ?", value = 400.0)

    loisir = st.number_input("Quel est le montant mensuel accordé à vos loisirs (activités, divertissement) ?", value = 400.0)

    personnel = st.number_input("Quel est le montant mensuel accordé à vos dépenses personnelles (vêtements, soins d'hygiène, cadeaux) ?", value = 200.0)

    économie = (salaire/12) - (habitation+alimentation+utilité+transport+loisir+personnel)
    

    #Interprétation des valeurs/Analyse du budget
    st.write("---")

    st.header('Résumé')

    #Division en deux colones 
    col1, col2 = st.columns([1,1], gap="medium")

    #Première colone - Indiquer les critères à respecter (if/else)
    with col1:
        #S'il reste des économies, indiquer le montant mensuel possible d'économiser
        if économie > 0:
            st.write(f"Avec vos dépenses actuels, il vous reste un total de :blue[{économie:.2f}$] disponible par mois.\n\n\nCe montant peut être donc placé dans l'optique de prévoir votre retraite.\n\n\nDans l'onglet **_Retraite_**, nous vous permettons de calculer le montant mensuel qui vous permetterait d'atteindre votre objectif de retraite.")
        
        #S'il n'y a pas d'économies, indiquer le montant mensuel qui dépasse les revenus
        else:
            st.write(f"Avec vos dépenses actuelles, il ne vous reste pas de montant disponible pour l'épargne. Vos dépenses dépassent ainsi de :blue[{(habitation+alimentation+utilité+transport+loisir+personnel)-(salaire/12):.2f}$] votre revenu mensuel.\n\n\nIl serait judicieux de revoir vos dépenses ou d'augmenter vos revenus afin de ne pas vous endettez.")

    #Deuxième colone - Graphique pointe de tarte
    with col2:
        #Réprésentation du budget s'il reste des économies
        if économie >= 0:
            labels = 'Économie', 'Habitation', 'Alimentation', 'Utilité', 'Transport', 'Loisir', 'Personnel'
            sizes = [(économie/salaire), (habitation/salaire), (alimentation/salaire), (utilité/salaire), (transport/salaire), (loisir/salaire), (personnel/salaire)]
            myexplode = [0.05, 0, 0, 0, 0, 0, 0]
            couleurs = ['#CC3363', '#C2F9BB', '#62C370', '#9AD1D4', '#26547C', '#3083DC', '#30C5FF']

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, explode = myexplode, colors = couleurs, autopct='%1.1f%%')
            ax1.axis('equal') 

            st.pyplot(fig1)
        
        #Recommandations s'il ne reste pas d'économies
        else:
            st.write(f"Dans l'onglet **_Retraite_**, nous vous permettons de calculer le montant mensuel qui vous permetterait d'atteindre votre objectif de retraite.")


#Deuxième volet - Retraite
with tab2:

    st.title(":blue[Retraite]\n")

    #Division en deux colones
    col1, col2 = st.columns(2, gap="medium")

    #Première colonne - Valeurs à indiquer pour planification retraite
    with col1:

        age = st.slider("Quel est votre âge ?", min_value=1, max_value=100, value=25, step=1)

        retraite = st.slider("À quelle âge souhaitez-vous prendre votre retraire ?", min_value=1, max_value=100, value=65, step=1)

    #Deuxième colonne - Valeurs à indiquer pour planification retraite (suite)
    with col2:
   
        st.subheader(f"Pour votre retraite dans {retraite-age} ans:")

        objectif = st.number_input("Quel est votre le montant que vous ciblez pour votre retraite ?", value = 500000.0)

        taux = st.number_input("Quel est le taux annuel que vous croyez pouvoir obtenir pour vos placements ?", value = 4.25)

        placement = st.number_input("Avez-vous déjà des placements ? Si oui, indiquez le montant.", value = 10000.0)

    #Autres valeurs utiles pour calcul du montant mensuel à économiser
    n = (retraite-age) * 12

    t = taux/100

    montant_retraite = objectif - (placement * ((1 + t) ** (retraite-age)))

    #Calcul du montant mensuel à économiser pour atteindre objectif de retraite
    montant_mensuel = (montant_retraite * t/12) / (((1+t/12)**n)-1)

    #Présentation du résultat en fonction des valeurs indiquées ci-dessus
    st.write("---")

    st.header('Résumé')

    st.write(f"Afin d'atteindre cet objectif, le montant à épargner mensuellement est de :blue[{montant_mensuel:.2f}$] si vous voulez atteindre votre objectif de {objectif:.2f}$ d'ici les {retraite-age} prochaines années.\n\n\nDans l'onglet **_Analyse_**, il vous sera possible de voir l'évolution de vos épargnes si vous économisez ce montant chaque mois.")


#Troisième volet - Analyse
with tab3:

    st.title(":blue[Analyse]\n")

    #Divison en deux colonnes
    col1, col2 = st.columns([1,2], gap="medium")

    #Première colonne - Description du graphique + Analyse budget
    with col1:
        st.write(f"Le graphique suivant illustre l'évolution de votre placement si vous épargnez mensuellement le montant de :blue[{montant_mensuel:.2f}$] à un taux annuel de {taux}% pendant {retraite-age} ans en tenant compte de votre placement actuel.")

        #Si assez d'économies pour objectif de retraite
        if économie > montant_mensuel:
            st.subheader(f":green[Bonne nouvelle !]")
            st.write(f"Avec votre budget actuel, il vous est possible d'atteindre cet objectif si vous prenez votre retraite à {retraite} ans. De plus, il vous resterait un montant de :orange[{(économie - montant_mensuel):.2f}$] en surplus par mois que vous pourriez utiliser pour d'autres dépenses/loisirs !")
        
        #Si économies insuffisantes
        else: 
            st.subheader(f":red[Mauvaise nouvelle ...]")
            st.write(f"Malheureusement, avec votre budget actuel, il vous est impossible d'atteindre cet objectif si vous prenez votre retraitre à {retraite} ans. Si vous désirez réellement cumulé un total de {objectif:.2f}$, vous devez soit revoir vos dépenses ou augmenter vos revenus. Trouver un taux de placement plus élevé ou bien retarder votre retraitre peuvent aussi vous aider à atteindre cet objectif financier.")


    #Deuxième colonne - Illustration graphique évolution du placement jusqu'à la retraite
    with col2:

        #Calcul des valeurs capitalisés de chaque année
        valeur_cap = []
        for i in range(retraite-age):
            valeur = (montant_mensuel * 12 *(1+t)** (i+1))
            valeur_cap.append(valeur)

        #Calcul des valeurs totales à chaque année
        valeur_roulante = []
        for i in range(retraite-age):
            valeur_total = sum(valeur_cap[0:(i+1)]) + placement * (1+t)**(i+1)
            valeur_roulante.append(valeur_total)

        #Graphique à barres
        st.bar_chart(data=valeur_roulante, x=None, y=None, width=0, height=0, use_container_width=True)


    

    
    

