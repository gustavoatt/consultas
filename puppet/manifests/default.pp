import "classes/init.pp"

$PROJECT_DIR = "/vagrant"

class dev {
  class {
    init:
  }
}

include dev
