	let SCENE;
	let CAMERA;
	let RENDERER;
	let LOADING_MANAGER;
	let IMAGE_LOADER;
	let OBJ_LOADER;
	let CONTROLS;
	let MOUSE;
	let RAYCASTER;
	let TEXTURE;
	let OBJECT;

	function initScene() {
    SCENE = new THREE.Scene();

    initLights();
}

function initLights() {
    const ambient = new THREE.AmbientLight(0xffffff, 0.7);
    SCENE.add(ambient);

    const directionalLight = new THREE.DirectionalLight(0xffffff);
    directionalLight.position.set(0, 1, 1);
    SCENE.add(directionalLight);
}
function initCamera() {
    CAMERA = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 2000);
    CAMERA.position.z = 100;
}

	function initRenderer() {
    RENDERER = new THREE.WebGLRenderer({ alpha: true });
    RENDERER.setPixelRatio(window.devicePixelRatio);
    RENDERER.setSize(window.innerWidth, window.innerHeight);
    THREE.MeshBasicMaterial({color:'red'})
}

function initLoaders() {
    LOADING_MANAGER = new THREE.LoadingManager();
    IMAGE_LOADER = new THREE.ImageLoader(LOADING_MANAGER);
    OBJ_LOADER = new THREE.OBJLoader(LOADING_MANAGER);
}
function loadModel() {
    OBJ_LOADER.load(model, (object) => {

        object.scale.x = 0.3;
        object.scale.y = 0.3;
        object.scale.z = 0.3;
        object.rotation.x = -Math.PI / 2;
        object.position.y = -30;

        OBJECT = object;
        SCENE.add(OBJECT);
    });
}

function render() {
    CAMERA.lookAt(SCENE.position);
    RENDERER.render( SCENE, CAMERA );
}
function animate() {
        requestAnimationFrame( animate );

    }
    animate();
initScene();
initLights();
initCamera();
initRenderer();
initLoaders();
loadModel();
render();
console.log(123)