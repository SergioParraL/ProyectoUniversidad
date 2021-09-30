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


