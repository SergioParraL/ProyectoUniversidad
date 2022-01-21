function tMenu () {
	const d = document
	let menu = d.getElementById('menu-Arrow')
	let mActive = d.getElementById('col_1')
	let MenuClass = menu.classList.contains('is-active')
	let hoverLi = document.getElementsByClassName('prin')
	let icon = document.querySelectorAll('.IconNav')

	if(MenuClass == true){
		menu.classList.remove('is-active')
		mActive.classList.remove('col_1_Active')
		for (var i = 0; i < hoverLi.length; i++) {
            hoverLi[i].classList.remove('active')
			icon[i].style.paddingLeft = '3em' 
        }
	}	
	else {
		menu.classList.add('is-active')
		mActive.classList.add('col_1_Active')
		for (var i = 0; i < hoverLi.length; i++) {
            hoverLi[i].classList.add('active')
			icon[i].style.paddingLeft = '2em' 
        }
	}
}

function tCardData () {
	// alert('entrando')
	const d = document
	const act = 'is-active'
	let icon = d.querySelector('#menuArrowCard')
	let mActive = icon.classList.contains(act)
	let card = d.querySelector('#card')

	let first = d.querySelector('.cardUserAct')
	let second = d.querySelector('.cardButtonDesp')

	if (mActive == true) {
		card.style.top = '-26.2vh'
		first.classList.remove('cardShadow')
		second.classList.remove('cardShadow')
		icon.classList.remove(act)
	}else {
		card.style.top = '0%'
		icon.classList.add(act)
		first.classList.add('cardShadow')
		second.classList.add('cardShadow')
	}
}


