echo '[Desktop Entry]' >> /usr/share/applications/Andspoilt.desktop
echo 'Type=Application' >> /usr/share/applications/Andspoilt.desktop
echo 'Name=Andspoilt' >> /usr/share/applications/Andspoilt.desktop
echo 'Encoding=UTF-8' >> /usr/share/applications/Andspoilt.desktop
echo 'Comment=Android Exploit Toolkit' >> /usr/share/applications/Andspoilt.desktop
echo 'Categories=08-exploitation-tools;Security;' >> /usr/share/applications/Andspoilt.desktop
echo "Exec=sh -c 'andspoilt;${SHELL:-bash}'" >> /usr/share/applications/Andspoilt.desktop
echo 'Icon=/usr/share/andspoilt/src/a.png' >> /usr/share/applications/Andspoilt.desktop
echo 'Terminal=true' >> /usr/share/applications/Andspoilt.desktop
