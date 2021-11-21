function buttonRegEst() {
	let registro = document.querySelector('.SigButton')
	let buttonSig = document.querySelector('#butSig')
	let left = document.querySelector('.Wleft')
	let right = document.querySelector('.Wright')
	if (right.classList.contains('hidden')) {
		registro.classList.remove('hidden')
		right.classList.remove('hidden')
		left.classList.add('hidden')
		buttonSig.textContent = 'Anterior'
	}else {
		right.classList.add('hidden')
		left.classList.remove('hidden')
		registro.classList.add('hidden')
		buttonSig.textContent = 'Siguiente'
	}
}

function buttonVerEstuRepr(){
	let left = document.querySelector('.Wleft')
	let right = document.querySelector('.Wright')
	let button = document.querySelector('#Ant_Sig')

	if (right.classList.contains('hidden')) {
		left.classList.add('hidden')	
		right.classList.remove('hidden')
		Ant_Sig.textContent = 'Ver: Estudiante'	
	}else {
		left.classList.remove('hidden')	
		right.classList.add('hidden')
		Ant_Sig.textContent = 'Ver: Representante'	
		
	}

}

