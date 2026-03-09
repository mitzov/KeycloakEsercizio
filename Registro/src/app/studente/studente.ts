import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../core/auth.service';

@Component({
  selector: 'app-studente',
  imports: [CommonModule],
  templateUrl: './studente.html',
  styleUrl: './studente.css',
})
export class StudenteComponent {
  constructor(public auth: AuthService) {}

  voti:any[] = [];

}