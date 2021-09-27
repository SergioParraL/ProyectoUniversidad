function changeValidateUserPA () {
	 	SwitchPA.classList.add('PA')
 	let PD = document.getElementById('PD').classList.add('WrapperHiddent')
 	let PA = document.getElementById('PA').classList.remove('WrapperHiddent')

}

function changeValidateUserPD(){
 	SwitchPD.classList.add('PD')
 	let PD = document.getElementById('PD').classList.remove('WrapperHiddent')
 	let PA = document.getElementById('PA').classList.add('WrapperHiddent')
}

function timer () {
	let time = window.setTimeout(closeLoader,1000)
}

function closeLoader() {
	loading.classList.add('close_loader')
 	let loadClass = document.getElementById('load').classList.remove('loader')
}