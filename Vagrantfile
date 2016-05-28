# 'Vagrantfile'.


Vagrant.configure(2) do | config |

  (1..3).each do | i |

    config.vm.define ('vm' + i.to_s).to_sym do | vm |

      vm.vm.box = 'centos/7'

      vm.vm.provider :libvirt do | domain |
        domain.memory = 2048
        domain.cpus = 4
        domain.nested = true
      end

      vm.vm.network 'private_network', ip: '192.168.40.1' + i.to_s

      vm.vm.synced_folder '.', '/home/vagrant/sync', type: 'rsync',
                          disabled: true

      vm.vm.synced_folder '.', '/vagrant', type: 'nfs',
                          :mount_options => [ 'nolock,vers=3,udp,noatime' ]

      vm.vm.provision 'shell', inline: <<-eof1
        echo vm#{i} > /etc/hostname
        /bin/systemctl restart systemd-hostnamed
      eof1

      vm.vm.provision 'shell', inline: <<-'eof1'
        ln -s -f /usr/share/zoneinfo/UTC /etc/localtime

        cat > /etc/profile.d/mecachis.sh <<'eof2'
[ `/bin/id -u` = "0" ] && PS1="\h# " || PS1="\h$ "
export PS1
eof2

        cat > /etc/rsyslog.d/udp.conf <<'eof2'
$ModLoad imudp
$UDPServerRun 514
eof2
        /bin/systemctl restart rsyslog.service

        cat > /etc/yum.repos.d/docker.repo <<'eof2'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
eof2
        yum -y install docker-engine
        systemctl enable docker.service
        systemctl start docker.service
      eof1
    end
  end
end
