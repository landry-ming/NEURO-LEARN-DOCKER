cd /nls-ml/app;
export C_FORCE_ROOT=true;
nohup celery worker -A main.celery --loglevel=info >> /nls-ml/log/celery.log &
gunicorn main:app --bind 0.0.0.0:4701 --workers 4 --log-level debug --access-logfile /nls-ml/log/gunicorn.access.log --error-logfile /nls-ml/log/gunicorn.error.log;
