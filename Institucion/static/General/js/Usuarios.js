window.onload = function(){
	let num = 0
	let sigButton = document.querySelector('.btnG')
	sigButton.addEventListener('click',TabChange)
	function TabChange(){
		console.log(num)
		let tab01 = document.querySelector('.Wright')
		let tab02 = document.querySelector('.Wleft')
		let registroButton = document.querySelector('.SigButton')
		if (num == 0){
			tab01.classList.remove('hidden')
			tab02.classList.add('hidden')
			sigButton.textContent = 'Ver: Estudiante'
			if (window.location.href == 'http://127.0.0.1:8000/Registro/Registro_Es/') {
				registroButton.classList.remove('hidden')
				sigButton.textContent = 'Anterior'
			}
			num = 1
		}else{
			tab02.classList.remove('hidden')
			tab01.classList.add('hidden')
			sigButton.textContent = 'Ver: Representante'
			if (window.location.href == 'http://127.0.0.1:8000/Registro/Registro_Es/') {
				registroButton.classList.add('hidden')
				sigButton.textContent = 'Siguiente'
			}
			num = 0
		}
	}
}



