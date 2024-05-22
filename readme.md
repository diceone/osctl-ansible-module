# osctl-ansible-module

This repository contains a custom Ansible module for interacting with the `osctl` API. The module supports various operations like retrieving system information, managing services, and more.

## Usage

### Prerequisites

- Ensure the `osctl` API server is running and accessible.
- Ensure you have the `requests` library installed in the Python environment that Ansible uses.

### Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/osctl-ansible-module.git
cd osctl-ansible-module
```

### Configuration

Update `ansible.cfg` to include the custom module library path:

```ini
[defaults]
library = ./library
```

### Example Playbook

An example playbook is provided in the `playbooks` directory. Here is how to run it:

```bash
ansible-playbook -i localhost, playbooks/osctl_playbook.yml
```

### Module Parameters

- `endpoint`: The API endpoint to call (e.g., `ram`, `disk`, `service`, etc.).
- `host`: The host where the `osctl` API server is running.
- `port`: The port on which the `osctl` API server is running.
- `username`: The username for basic authentication.
- `password`: The password for basic authentication.
- `params`: Additional parameters for the API call (used for specific endpoints like `service`).

### Example Usage in Playbook

```yaml
- name: Get RAM usage
  osctl_module:
    endpoint: "ram"
    host: "localhost"
    port: 12000
    username: "admin"
    password: "password"
  register: result

- name: Display RAM usage
  debug:
    msg: "{{ result.original_message }}"
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
