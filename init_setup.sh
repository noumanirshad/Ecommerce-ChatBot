echo [$(date)]: "START"
touch .env
echo [$(date)]: "Creating conda env with python 3.8"
conda create --prefix ./env python=3.9 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "intalling requirements"
pip install -r requirements.txt
echo [$(date)]: "END"
