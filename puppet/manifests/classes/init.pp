class init {
  group { "puppet":
    ensure => "present",
  }

  # Update the system.
  exec {"update-apt":
    command => "/usr/bin/apt-get update",
  }

  # Install python and dev utils.
  package {
    ["python", "python-dev", "libjs-jquery", "libjs-jquery-ui", "iso-codes",
    "gettext", "python-pip", "bzr", "zsh", "vim"]:
    ensure  => installed,
    require => Exec["update-apt"],
  }

  # Let's install the project dependecies from pip.
  exec { "pip-install-requirements":
      command => "/usr/bin/pip install -r ${PROJECT_DIR}/requirements/local.txt",
      tries => 2,
      timeout => 600, # Too long, but this can take a while
      require => Package["python-pip", "python-dev"],
      logoutput => on_failure,
  }

  # Oh my zsh.
  class { "ohmyzsh": }
  ohmyzsh::install { "vagrant": }
  ohmyzsh::theme { 'vagrant': theme => 'bureau' }
  ohmyzsh::plugins { 'vagrant': plugins => 'git django heroku ' }

  $MANAGE_FILE="/vagrant/consultas_proyecto/manage.py"
  file_line { 'run_test_alias':
    path  => '/home/vagrant/.zshrc',
    line  => "alias run_test=\'python ${MANAGE_FILE} test --settings=consultas_proyecto.settings.test\'",
    require => [Package["zsh"], Class['ohmyzsh'], Ohmyzsh::Install['vagrant']],
  }

  file_line { 'run_server_alias':
    path  => '/home/vagrant/.zshrc',
    line  => "alias run_server=\'python ${MANAGE_FILE} run_gunicorn 0.0.0.0:8000 --settings=consultas_proyecto.settings.local\'",
    require => [Package["zsh"], Class['ohmyzsh'], Ohmyzsh::Install['vagrant']],
  }

  file_line { 'syncdb_alias':
    path  => '/home/vagrant/.zshrc',
    line  => "alias syncdb=\'python ${MANAGE_FILE} syncdb --settings=consultas_proyecto.settings.local && python ${MANAGE_FILE} migrate --settings=consultas_proyecto.settings.local\'",
    require => [Package["zsh"], Class['ohmyzsh'], Ohmyzsh::Install['vagrant']],
  }
}
