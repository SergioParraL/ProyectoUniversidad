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

function opeWithDate(){
	const dateC = new Date()
	const yOld = document.querySelector('#id_edad')

	// Format of the date => Year - Month - Day
	
	const dateInput = [parseInt(this.value.substr(0,4)),parseInt(this.value.substr(5,2)),parseInt(this.value.substr(8))]
	const dateNow = [dateC.getFullYear(),dateC.getMonth() + 1 ,dateC.getDay() - 1]
	let yearOld = dateNow[0] - dateInput[0]

	if (dateInput[1] > dateNow[1]){
		yearOld--
	}if(dateInput[1] == dateNow[1]){
		if(dateInput[2] > dateNow[2]){
			yearOld--
		}
	}
	yOld.value = yearOld
	yOld.setAttribute('readonly','readonly')
}
