// State Pattern

const textState = function(){
	let currentState = new aboutState(this);
	
	this.init = function(){
		this.change(new aboutState);
	}
	
	this.change = function(state){
		currentState = state;
	}

};


const aboutState = function(page){
	document.querySelector('#heading').textContent = 'About';
	document.querySelector('#content').innerHTML = `
	<p>
	Belga, nascido em 1988. Trabalhou como consultor de
	vendas e como agente de suporte técnico para
	empresas como Groupon, Cisco, Belkin e GoDaddy.
	Programador autodidata e com aprendizado contínuo.
	Estou procurando uma função onde possa crescer e continuar
	a aprender com outros membros experientes da equipe.
	</p>
	`;
};

const educationState = function(page){
	document.querySelector('#heading').textContent = 'Educação';
	document.querySelector('#content').innerHTML = `
	<p>
	Ensino Médio | Design Gráfico <br>
	Faculdade (incompleto) | Design Gráfico <br>
	</p>
	`;
};


const workState = function(page){
	document.querySelector('#heading').textContent = 'Trabalho';
	document.querySelector('#content').innerHTML = `
	<p>
	Trabalhei para as seguintes empresas:<br>
	Polifonia, Suporte Técnico, São Paulo, BR<br>
	GoDaddy, Suporte Técnico, Belfast, Reino Unido<br>
	Cisco, consultor de pré-vendas, Belfast, Reino Unido<br>
	Groupon, Consultor de Vendas, Bruxelas, BE<br>
	CY, Consultor de Vendas, Ghent, BE<br>
	</p>
	`;
};

// Instantiate the page
const page = new textState();

// Init the first state
page.init();

// UI variables
const about = document.getElementById('about'),
      education = document.getElementById('education'),
      work = document.getElementById('work');
      
// About
about.addEventListener('click', (e) => {
	page.change(new aboutState);
	
	e.preventDefault();
});
	   
	   
//  Education
education.addEventListener('click', (e) =>{
	page.change(new educationState);
	
	e.preventDefault();
});

// Work
work.addEventListener('click', (e)	=> {
	page.change(new workState);
	
	e.preventDefault();
});     